import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

class ModelEvaluator:
    """
    Kursun 15. Bölümünde (Karmaşıklık Matrisi - Confusion Matrix) ve 
    20. Bölümünde (Model Değerlendirme & Kıyaslama) öğretilen analizleri üretir.
    """
    @staticmethod
    def plot_confusion_matrix(cm, class_names, title="Karmaşıklık Matrisi (Confusion Matrix)"):
        """
        Matplotlib ve Seaborn kullanarak Confusion Matrix ısı haritası çizer.
        """
        fig, ax = plt.subplots(figsize=(6, 5))
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=class_names,
            yticklabels=class_names,
            ax=ax,
            cbar=False
        )
        ax.set_xlabel("Tahmin Edilen Sınıf (Predicted)", fontsize=11, fontweight="bold")
        ax.set_ylabel("Gerçek Sınıf (True Label)", fontsize=11, fontweight="bold")
        ax.set_title(title, fontsize=12, fontweight="bold", pad=12)
        plt.tight_layout()
        return fig

    @staticmethod
    def get_benchmark_dataframe(benchmark_dict):
        """
        Modellerin 5-Katlı Çapraz Doğrulama (CV) ve Test Doğruluklarını DataFrame tablosu yapar.
        """
        rows = []
        for name, data in benchmark_dict.items():
            rows.append({
                "Model Adı": name,
                "5-Fold CV Doğruluğu (%)": round(data["cv_mean"] * 100, 2),
                "Test Seti Doğruluğu (%)": round(data["test_accuracy"] * 100, 2)
            })
        df = pd.DataFrame(rows).sort_values("Test Seti Doğruluğu (%)", ascending=False)
        return df

    @staticmethod
    def plot_benchmark_comparison(df_benchmark):
        """
        Algoritmaların test skorlarını kıyaslayan şık bir sütun grafiği çizer.
        """
        fig, ax = plt.subplots(figsize=(7, 4))
        bars = ax.bar(
            df_benchmark["Model Adı"],
            df_benchmark["Test Seti Doğruluğu (%)"],
            color=["#2b5c8f", "#3c8dbc", "#5dade2", "#aed6f1"]
        )
        ax.set_ylim(0, 105)
        ax.set_ylabel("Doğruluk Skoru (Accuracy %)", fontsize=11, fontweight="bold")
        ax.set_title("Makine Öğrenmesi Algoritmaları Kıyaslama Sonuçları", fontsize=12, fontweight="bold")
        
        # Sütunların üzerine yüzde değerlerini yaz
        for bar in bars:
            height = bar.get_height()
            ax.annotate(
                f"%{height:.1f}",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontweight="bold"
            )
        plt.tight_layout()
        return fig

if __name__ == "__main__":
    sample_cm = np.array([
        [35, 1, 0, 0],
        [2, 34, 0, 0],
        [0, 1, 35, 0],
        [1, 0, 0, 35]
    ])
    classes = ["Backend", "Data Science", "DevOps", "Frontend"]
    fig = ModelEvaluator.plot_confusion_matrix(sample_cm, classes)
    print("ModelEvaluator başarıyla çalıştı.")

