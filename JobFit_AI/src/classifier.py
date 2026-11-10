import os
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

try:
    from .nlp_preprocessor import NLPPreprocessor
except (ImportError, ValueError):
    from JobFit_AI.src.nlp_preprocessor import NLPPreprocessor

class JobClassifierTrainer:
    """
    Kursun 10, 11, 12, 14, 15 ve 20. bölümlerindeki algoritmaları
    iş ilanları ve CV metinleri üzerinde eğiten ve kıyaslayan sınıflandırma sınıfı.
    
    Yarıştırılan Algoritmalar:
    - Naive Bayes (MultinomialNB - Bölüm 12)
    - K-Nearest Neighbors (KNN - Bölüm 10)
    - Support Vector Machine (SVM - Bölüm 11)
    - Random Forest (Bölüm 14)
    """
    def __init__(self, data_path=None):
        if data_path is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            data_path = os.path.join(base_dir, "data", "job_postings.csv")
        self.data_path = data_path
        self.preprocessor = NLPPreprocessor(max_features=2500)
        
        self.models = {
            "Naive Bayes": MultinomialNB(),
            "KNN": KNeighborsClassifier(n_neighbors=5),
            "SVM": SVC(kernel="linear", probability=True, random_state=42),
            "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
        }
        self.best_role_model = None
        self.best_role_name = ""
        self.level_model = None
        self.benchmark_results = {}

    def load_and_preprocess_data(self):
        df = pd.read_csv(self.data_path)
        # Metinleri temizle
        df["Cleaned_Desc"] = df["Description"].apply(self.preprocessor.clean_text)
        return df

    def train_and_benchmark_roles(self):
        """
        Tüm modelleri eğitir, test setinde ve 5-Katlı Çapraz Doğrulama (K-Fold CV) ile kıyaslar.
        """
        df = self.load_and_preprocess_data()
        X_raw = df["Cleaned_Desc"].values
        y = np.array(df["Role"].tolist(), dtype=object)

        # TF-IDF vektörleştirme
        X = self.preprocessor.vectorizer.fit_transform(X_raw)
        self.preprocessor.is_fitted = True

        # Train-Test Split (%80 Eğitim, %20 Test)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        results = {}
        best_acc = 0.0

        for name, model in self.models.items():
            # 5-Katlı Çapraz Doğrulama (K-Fold CV - Bölüm 20)
            cv_scores = cross_val_score(model, X_train, y_train, cv=5)
            
            # Modeli eğit
            model.fit(X_train, y_train)
            
            # Test seti tahminleri
            y_pred = model.predict(X_test)
            test_acc = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred, output_dict=True)
            cm = confusion_matrix(y_test, y_pred)

            results[name] = {
                "cv_mean": float(np.mean(cv_scores)),
                "cv_std": float(np.std(cv_scores)),
                "test_accuracy": float(test_acc),
                "report": report,
                "confusion_matrix": cm,
                "model": model
            }

            if test_acc > best_acc:
                best_acc = test_acc
                self.best_role_name = name
                self.best_role_model = model

        self.benchmark_results = results

        # Ayrıca Kıdem Seviyesi (Level: Junior, Mid, Senior) modelini eğit
        y_level = np.array(df["Level"].tolist(), dtype=object)
        X_tr_l, X_te_l, y_tr_l, y_te_l = train_test_split(
            X, y_level, test_size=0.2, random_state=42, stratify=y_level
        )
        self.level_model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.level_model.fit(X_tr_l, y_tr_l)
        level_acc = accuracy_score(y_te_l, self.level_model.predict(X_te_l))

        return {
            "role_benchmark": results,
            "best_role_model": self.best_role_name,
            "best_accuracy": best_acc,
            "level_accuracy": float(level_acc),
            "classes": sorted(list(np.unique(y)))
        }

    def predict_role_and_level(self, text):
        """
        Herhangi bir CV veya iş ilanı metninin rolünü ve seviyesini tahmin eder.
        """
        if self.best_role_model is None or self.level_model is None:
            raise ValueError("Modeller henüz eğitilmedi veya yüklenmedi!")
            
        cleaned = self.preprocessor.clean_text(text)
        vec = self.preprocessor.vectorizer.transform([cleaned])

        role_pred = self.best_role_model.predict(vec)[0]
        role_probs = self.best_role_model.predict_proba(vec)[0]
        role_conf = float(np.max(role_probs))

        level_pred = self.level_model.predict(vec)[0]
        level_probs = self.level_model.predict_proba(vec)[0]
        level_conf = float(np.max(level_probs))

        return {
            "predicted_role": role_pred,
            "role_confidence": round(role_conf * 100, 1),
            "predicted_level": level_pred,
            "level_confidence": round(level_conf * 100, 1)
        }

    def save_artifacts(self, models_dir=None):
        if models_dir is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            models_dir = os.path.join(base_dir, "models")
        os.makedirs(models_dir, exist_ok=True)

        joblib.dump(self.preprocessor.vectorizer, os.path.join(models_dir, "tfidf_vectorizer.joblib"))
        joblib.dump(self.best_role_model, os.path.join(models_dir, "role_classifier.joblib"))
        joblib.dump(self.level_model, os.path.join(models_dir, "level_classifier.joblib"))
        
        # Kıyaslama sonuçlarını da görselleştirme için kaydet
        benchmark_summary = {
            name: {
                "cv_mean": res["cv_mean"],
                "test_accuracy": res["test_accuracy"],
                "confusion_matrix": res["confusion_matrix"].tolist()
            }
            for name, res in self.benchmark_results.items()
        }
        joblib.dump(benchmark_summary, os.path.join(models_dir, "benchmark_summary.joblib"))
        print(f"Tüm modeller ve vektörleştirici kaydedildi: {models_dir}")

    def load_artifacts(self, models_dir=None):
        if models_dir is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            models_dir = os.path.join(base_dir, "models")

        self.preprocessor.vectorizer = joblib.load(os.path.join(models_dir, "tfidf_vectorizer.joblib"))
        self.preprocessor.is_fitted = True
        self.best_role_model = joblib.load(os.path.join(models_dir, "role_classifier.joblib"))
        self.level_model = joblib.load(os.path.join(models_dir, "level_classifier.joblib"))

if __name__ == "__main__":
    trainer = JobClassifierTrainer()
    print("Modeller eğitiliyor ve kıyaslanıyor (KNN, SVM, Naive Bayes, Random Forest)...")
    summary = trainer.train_and_benchmark_roles()
    
    print("\n--- MODEL BENCHMARK SONUÇLARI ---")
    for name, res in summary["role_benchmark"].items():
        print(f"Model: {name:<15} | 5-Fold CV: %{res['cv_mean']*100:.2f} | Test Doğruluğu: %{res['test_accuracy']*100:.2f}")

    print(f"\nEn Başarılı Rol Modeli: {summary['best_role_model']} (%{summary['best_accuracy']*100:.2f})")
    print(f"Kıdem Seviyesi Modeli Test Doğruluğu: %{summary['level_accuracy']*100:.2f}")

    # Örnek test tahmini
    sample = "Building deep learning architectures, training PyTorch neural networks, running exploratory data analysis with Pandas."
    pred = trainer.predict_role_and_level(sample)
    print("\nÖrnek Metin Tahmini:")
    print(pred)

    trainer.save_artifacts()

