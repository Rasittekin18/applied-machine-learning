# 📈 Applied Machine Learning & Data Analytics Showcase

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-v1.x-orange?logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Scientific-013243?logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-teal)

<br/>

**A production-ready collection of Applied Machine Learning models, Exploratory Data Analysis (EDA) case studies, and 60+ algorithmic notebooks.**  
Developed by **[Raşit Tekin](https://github.com/Rasittekin18)**.

[Projeler Tablosu](#-projeler-ve-modüller) • [Kurulum & Çalıştırma](#-kurulum-ve-kullanım) • [Teknolojiler](#-kullanılan-teknolojiler) • [İletişim](#-yazar)

</div>

---

## 📌 Genel Bakış (Overview)

Bu depo; sağlık, otomotiv, çevre ve uzay veri setleri üzerinde geliştirilmiş **uçtan uca makine öğrenmesi tahmin modellerini**, detaylı **keşifçi veri analizi (EDA)** çalışmalarını ve sıfırdan ileri seviyeye kadar algoritmaların matematiksel temellerini ele alan **kapsamlı eğitim serilerini** içerir.

Tüm projeler kendi veri setleri, bağımsız çalıştırma scriptleri ve Jupyter notebook'ları ile alt klasörlerde eksiksiz korunmaktadır.

---

## 📂 Projeler ve Modüller

### 1. 🎯 Uçtan Uca Tahmin & Sınıflandırma Modelleri
| # | Proje Adı | Açıklama | Algoritmalar / Yöntemler | Klasör Linki |
| :-: | :--- | :--- | :--- | :-: |
| 01 | **Vehicle Fuel Consumption Prediction** | Auto-MPG veri seti üzerinde araç özellikleri (silindir, beygir gücü, ağırlık) ile yakıt tüketimi (MPG) tahmin modeli. | Linear Regression, Polynomial Reg, Scikit-Learn | [`/Vehicle-Fuel-Consumption-Prediction`](./Vehicle-Fuel-Consumption-Prediction) |
| 02 | **Ensemble Learning Framework** | Zayıf sınıflandırıcıları birleştirerek genelleme performansını artıran topluluk öğrenmesi mimarisi. | Random Forest, VotingClassifier, Bagging, Boosting | [`/Ensemble-Learning`](./Ensemble-Learning) |
| 03 | **Heart Attack Risk Prediction** | Klinik sağlık göstergeleri (tansiyon, kolesterol, kalp atışı) üzerinden kalp krizi riskini tespit eden sınıflandırma modeli. | Logistic Regression, Decision Trees, KNN, Random Forest | [`/heart-attack-analysis-prediction`](./heart-attack-analysis-prediction) |
| 04 | **Breast Cancer Classification** | Biyopsi hücre çekirdeği özellikleri üzerinden tümörün iyi/kötü huylu olduğunu tespit eden medikal teşhis modeli. | SVM, Logistic Regression, Feature Scaling | [`/breast-cancer-classification`](./breast-cancer-classification) |
| 05 | **Titanic Survival Prediction** | Yolcu demografisi, bilet sınıfı ve kabin verileriyle hayatta kalma olasılığını tahmin eden klasik veri bilimi projesi. | Feature Engineering, Random Forest, Imputation | [`/Titanic_Project`](./Titanic_Project) |

---

### 2. 📊 Keşifçi Veri Analizi (EDA) Vaka Çalışmaları
| # | Proje Adı | Açıklama | Görselleştirme & Analiz | Klasör Linki |
| :-: | :--- | :--- | :--- | :-: |
| 06 | **Water Quality & Potability Analysis** | pH, sertlik, kloraminler ve bulanıklık gibi fizikokimyasal parametrelerle suyun içilebilirliğini analiz eden çalışma. | Seaborn, Matplotlib, Correlation Heatmaps | [`/water-quality-analysis`](./water-quality-analysis) |
| 07 | **World Happiness Report Analysis** | Ülkelerin kişi başına düşen GSYİH, sosyal destek, yaşam beklentisi ve özgürlük metriklerinin mutluluk skoruna etkisinin analizi. | Plotly, Pandas, Multivariate EDA | [`/world-happiness-eda`](./world-happiness-eda) |
| 08 | **Space Mission Analytics** | Tarihsel uzay fırlatma görevlerinin başarı/başarısızlık oranları, bütçeleri ve fırlatıcı ülkelerin zaman serisi analitiği. | Time-Series EDA, Pandas, Matplotlib | [`/space-mission-data-analysis`](./space-mission-data-analysis) |

---

### 3. 🧠 Kapsamlı Makine Öğrenmesi Algoritma Kütüphanesi
| # | Modül Adı | İçerik & Kapsam | Notebook Sayısı | Klasör Linki |
| :-: | :--- | :--- | :-: | :-: |
| 09 | **Machine Learning Fundamentals (Part 1)** | Basit/Çoklu Regresyon, Lojistik Regresyon, KNN, SVM, Naive Bayes, Karar Ağaçları, Random Forest, K-Means, Hiyerarşik Kümeleme, PCA ve Model Seçimi. | 19 Notebook | [`/4-Machine_Learning`](./4-Machine_Learning) |
| 10 | **Advanced Machine Learning & Theory (Part 2)** | Bias-Variance Tradeoff, Boyut Laneti (Curse of Dimensionality), OLS Tablosu Okuma, Hipotez Testleri, Gradient Descent, GridSearch, L1/L2 Regularization ve Boosting modelleri. | 45 Notebook | [`/4-Machine_Learning_2`](./4-Machine_Learning_2) |

---

## 🚀 Kurulum ve Kullanım

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/Rasittekin18/applied-machine-learning.git
cd applied-machine-learning
```

### 2. Sanal Ortam Oluşturun
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Gerekli Kütüphaneleri Yükleyin
```bash
pip install numpy pandas scikit-learn matplotlib seaborn plotly scipy jupyter
```

### 4. Notebook'ları veya Python Kodlarını Çalıştırın
```bash
# Jupyter Arayüzünü Başlatma
jupyter notebook

# Python Scripti Çalıştırma (Örnek: Yakıt Tüketimi Tahmini)
cd Vehicle-Fuel-Consumption-Prediction
python Vehicle_Fuel_Consumption_Prediction.py
```

---

## 🛠️ Kullanılan Teknolojiler

- **Programlama:** Python 3.8+
- **Veri Manipülasyonu & İstatistik:** Pandas, NumPy, SciPy
- **Makine Öğrenmesi:** Scikit-Learn (Regresyon, Sınıflandırma, Kümeleme, Boyut İndirgeme, Ensemble Modelleri)
- **Görselleştirme:** Matplotlib, Seaborn, Plotly
- **Geliştirme Ortamı:** Jupyter Notebook, VS Code

---

## 👨‍💻 Yazar

**Raşit Tekin**  
*Electronics Engineer \| AI & Data Science*  
- GitHub: [@Rasittekin18](https://github.com/Rasittekin18)  
- E-posta: [rasittekin18@gmail.com](mailto:rasittekin18@gmail.com)  
- Konum: İstanbul, Türkiye

---

## 📄 Lisans

Bu repo kapsamındaki tüm projeler **MIT Lisansı** ile lisanslanmıştır.
