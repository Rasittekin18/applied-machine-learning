# 🤖 Machine Learning End-to-End Course & Applied Projects

Bu depo, Musa Arda tarafından verilen **Machine Learning** eğitiminin tüm teorik notlarını, matematiksel altyapısını, notasyon standartlarını ve Python üzerindeki uygulamalı projelerini içermektedir.

Eğitim boyunca hem teorik kavramlar (*Bias-Variance Trade-off*, *Curse of Dimensionality*, *Gözetimli/Gözetimsiz Öğrenme*, *Cross-Validation*) derinlemesine incelenmiş hem de Scikit-Learn, Pandas, NumPy, Statsmodels ve Seaborn kütüphaneleri kullanılarak gerçek hayat projeleri geliştirilmiştir.

---

## 📌 Müfredat ve Bölüm Yapısı

Proje reposu, kurs müfredatını adım adım takip eden Jupyter Notebook dosyalarından oluşmaktadır:

- **Bölüm 1 - 2: Genel Bakış & Kurulumlar**
  - Makine öğrenmesi ve Derin öğrenme farkı.
  - Anaconda, Jupyter Lab, Notion entegrasyonu ve Python sanal ortam yönetimi (`conda`).
- **Bölüm 3 - 4: ML Giriş Kavramları, Notasyon & Öğrenme Teorisi**
  - Vektör ve matris gösterimleri ($X \in \mathbb{R}^{n 	imes p}$, $y \in \mathbb{R}^n$).
  - $f$ fonksiyonunu tahmin etme, *Curse of Dimensionality*, *Overfitting vs. Underfitting*.
  - Parametrik ve Non-Parametrik model yaklaşımları.
- **Bölüm 5: Model Doğruluğunu Ölçmek**
  - *Bias-Variance Trade-off* dengesi.
  - Regresyon metrikleri: $MSE$, $RMSE$, $R^2$.
  - Sınıflandırma metrikleri: *Error Rate*, $K$-NN temel mantığı.
- **Bölüm 6 - 8: Regresyon Modelleri & Uygulamaları**
  - Basit Lineer Regresyon ve Çoklu Lineer Regresyon.
  - $OLS$ (Ordinary Least Squares) tablosu okuma, $p$-value, $t$-stat ve $F$-stat analizi.
  - Gerçek veri üzerinde Uçtan Uca Lineer Regresyon Projesi.
- **Bölüm 9: Gradient Descent (Optimizasyon)**
  - Gradient Descent matematiği, Learning Rate seçimi, Stochastic Gradient Descent (SGD).
- **Bölüm 10 - 12: Temel Sınıflandırma Modelleri**
  - **KNN (K-Nearest Neighbors):** Komşuluk parametreleri ve mesafe metrikleri.
  - **Naive Bayes:** Bayes Teoremi ve olasılıksal sınıflandırma.
  - **Lojistik Regresyon:** Sigmoid fonksiyonu, karar sınırları ve binary classification.
- **Bölüm 13 - 15: Performans Metrikleri, Model Seçimi & Regülarizasyon**
  - *Confusion Matrix*, *Precision*, *Recall*, *F1-Score*, *ROC-AUC*, *Log-Loss*.
  - $k$-Fold Cross-Validation ve Grid Search CV ile hiperparametre optimizasyonu.
  - Overfitting önleme: Ridge ($L_2$) ve Lasso ($L_1$) Regülarizasyon teknikleri.
- **Bölüm 16 - 18: Kompleks Modeller & Ensemble Teknikleri**
  - **Support Vector Machines (SVM):** Margin maximisation, Slack variables ve Kernel Trick (RBF, Poly).
  - **Decision Trees (Karar Ağaçları):** Gini Impurity, Entropy, Pruning.
  - **Random Forests (Bagging):** Ağaç toplulukları ve out-of-bag değerlendirmesi.
- **Bölüm 19 - 20: İleri Seviye & Unsupervised Learning**
  - **Boosting Algoritmaları:** AdaBoost, Gradient Boosting, XGBoost mantığı.
  - **Unsupervised Learning:** K-Means Clustering ve PCA (Principal Component Analysis) boyut indirgeme.

---

---

## 🛠️ Kurulum ve Çalıştırma

### 1. Repoyu Klonlayın
```bash
git clone https://github.com/Rasittekin18/4-Machine_Learning_2.git
cd 4-Machine_Learning_2
```

### 2. Conda Sanal Ortamı Oluşturun ve Aktif Edin
```bash
conda create --name ml_env python=3.8 -y
conda activate ml_env
```

### 3. Gerekli Kütüphaneleri Yükleyin
```bash
conda install jupyterlab pandas numpy matplotlib seaborn scikit-learn statsmodels -y
```

### 4. Jupyter Lab'i Başlatın
```bash
jupyter lab
```

---

## 🎯 Örnek Kullanım (Python)

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Train-Test Ayrımı
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. Model Eğitimi
model = LinearRegression()
model.fit(X_train, y_train)

# 3. Tahmin ve Değerlendirme
y_pred = model.predict(X_test)
print(f"MSE: {mean_squared_error(y_test, y_pred):.4f}")
print(f"R^2 Score: {r2_score(y_test, y_pred):.4f}")
```

---
