# 📈 Applied Machine Learning & Data Analytics Showcase

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-v1.x-orange?logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Scientific-013243?logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-teal)

<br/>

**A production-ready collection of Applied Machine Learning models, NLP-driven Web Applications, Exploratory Data Analysis (EDA) case studies, and 60+ algorithmic notebooks.**  
Developed by **[Raşit Tekin](https://github.com/Rasittekin18)**.

[🌟 JobFit AI Web App](#-öne-çıkan-uygulama-jobfit-ai) • [Projeler Tablosu](#-projeler-ve-modüller) • [Kurulum & Çalıştırma](#-kurulum-ve-kullanım) • [Teknolojiler](#-kullanılan-teknolojiler) • [İletişim](#-yazar)

</div>

---

## 📌 Genel Bakış (Overview)

Bu depo; uçtan uca doğal dil işleme (NLP) ve tavsiye motoru tabanlı **akıllı web uygulamalarını**, sağlık, otomotiv, çevre ve uzay veri setleri üzerinde geliştirilmiş **makine öğrenmesi tahmin modellerini**, detaylı **keşifçi veri analizi (EDA)** çalışmalarını ve sıfırdan ileri seviyeye algoritmaların matematiksel temellerini ele alan **kapsamlı eğitim serilerini** içerir.

Tüm projeler kendi veri setleri, bağımsız çalıştırma scriptleri, birim testleri veya Jupyter notebook'ları ile alt klasörlerde eksiksiz korunmaktadır.

---

## 🌟 Öne Çıkan Uygulama: JobFit AI

### 🎯 JobFit AI: Akıllı CV & İş İlanı Uygunluk Analizörü ve Beceri Tavsiye Motoru
> **Doğal Dil İşleme (NLP), Çoklu Model Kıyaslama (Benchmark) ve Streamlit ile Geliştirilmiş Akıllı Kariyer & ATS Optimizasyon Asistanı**

[![JobFit AI Klasörüne Git](https://img.shields.io/badge/Proje%20Klasörü-JobFit__AI-success?style=for-the-badge&logo=github)](./JobFit_AI)
[![Pytest Suite](https://img.shields.io/badge/Unit%20Tests-25%20Passed-brightgreen?style=for-the-badge&logo=pytest)](./JobFit_AI/tests)

**JobFit AI**, adayların PDF, Word (.docx) veya düz metin formatındaki özgeçmişlerini iş ilanlarıyla hem anlamsal (semantic) hem de teknik beceri bazında kıyaslayan, eksik becerileri listeleyip ATS (Aday Takip Sistemi) tavsiyeleri üreten ve makine öğrenmesi ile rol/seviye tahmini yapan **tam teşekküllü bir web uygulamasıdır**.

```
   ┌──────────────────┐       ┌──────────────────────┐
   │  PDF / DOCX CV   │       │  Hedef İş İlanı      │
   └────────┬─────────┘       └──────────┬───────────┘
            │                            │
            ▼                            ▼
   ┌─────────────────────────────────────────────────┐
   │    NLP Preprocessor (Regex Cleaner & Stemmer)   │
   └────────────────────────┬────────────────────────┘
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
   ┌──────────────────┐            ┌─────────────────┐
   │ TF-IDF Vektörü   │            │ 100+ Beceri     │
   │ & Cosine Sim.    │            │ Eşleştirme      │
   └────────┬─────────┘            └────────┬────────┘
            │                               │
            └───────────────┬───────────────┘
                            ▼
     ┌─────────────────────────────────────────────┐
     │   Hibrit Fit Skoru (%40 Semantik + %60 Beceri) │
     │   + Eksik Beceri Boşluk Analizi             │
     │   + 4 Boyutlu Plotly Radar Yetkinlik Grafiği│
     │   + ML Rol & Seviye Tahmini (NB/SVM/RF/KNN) │
     └─────────────────────────────────────────────┘
```

#### ✨ Temel Yetenekler
- **Çok Formatlı CV Ayrıştırma:** PyMuPDF ve python-docx kütüphaneleriyle PDF, Word DOCX ve TXT dosyalarından hatasız metin çıkarımı.
- **Teknoloji Koruyucu NLP Motoru:** C++, C#, .NET, Node.js gibi özel yazılım terimlerini ve son ekleri bozmayan özel regex tokenizasyon ve kök bulma mantığı.
- **Hibrit Uygunluk Skoru (0-100%):** `%40 TF-IDF Semantik Benzerlik + %60 Beceri Kapsama Oranı` ile hesaplanan güvenilir eşleşme metriği.
- **Eksik Yetenek (Skill Gap) & ATS Tüyoları:** 100+ teknik terim kütüphanesi üzerinden ilanda istenen fakat CV'de bulunmayan becerileri tespit edip mülakat öncesi ATS önerileri sunar.
- **Plotly İnteraktif Radar Grafiği:** Adayın profilini Data Science, Backend, Frontend ve DevOps boyutlarında görselleştirir.
- **Çoklu Model ML Sınıflandırıcı & Benchmark:** Naive Bayes, K-Nearest Neighbors, Destek Vektör Makineleri (SVM) ve Random Forest modellerini 5-Fold Cross Validation ile kıyaslar ve en yüksek doğruluğa sahip modelle rol/seviye tahmini yapar.
- **Tek Tıkla Rapor Dışa Aktarma:** Analiz özetini, uygunluk skorunu ve önerileri anında Markdown raporu olarak indirme imkanı.

👉 **Ayrıntılı teknik dokümantasyon, ekran görüntüleri ve kurulum için:** [`/JobFit_AI/README.md`](./JobFit_AI/README.md)

---

## 📂 Projeler ve Modüller

### 1. 🎯 Uçtan Uca Web Uygulamaları & Tahmin Modelleri
| # | Proje Adı | Açıklama | Algoritmalar / Yöntemler | Klasör Linki |
| :-: | :--- | :--- | :--- | :-: |
| 🌟 | **JobFit AI (Akıllı CV Analizörü)** | PDF/DOCX CV ve iş ilanlarını semantik NLP ve TF-IDF ile eşleştiren, eksik beceri analizi yapan ve makine öğrenmesiyle rol/seviye sınıflandıran interaktif Streamlit uygulaması. | TF-IDF, Cosine Similarity, SVM, Random Forest, Naive Bayes, KNN, Streamlit, Plotly | [`/JobFit_AI`](./JobFit_AI) |
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
| :-: | :--- | :--- | :--- | :-: |
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
pip install numpy pandas scikit-learn matplotlib seaborn plotly scipy jupyter streamlit pymupdf python-docx pytest
```

### 4. JobFit AI Web Uygulamasını Başlatın
```bash
# JobFit AI klasörüne geçin ve Streamlit sunucusunu başlatın
cd JobFit_AI
streamlit run app.py
```
> Web tarayıcınızda otomatik olarak `http://localhost:8501` adresi açılacaktır.

### 5. Testleri Çalıştırın
```bash
# JobFit AI test paketini çalıştırma (25/25 birim ve entegrasyon testi)
pytest JobFit_AI/tests -v
```

### 6. Diğer Script ve Notebook'ları Çalıştırma
```bash
# Jupyter Arayüzünü Başlatma
jupyter notebook

# Örnek Python Scripti Çalıştırma (Yakıt Tüketimi Tahmini)
cd Vehicle-Fuel-Consumption-Prediction
python Vehicle_Fuel_Consumption_Prediction.py
```

---

## 🛠️ Kullanılan Teknolojiler

- **Programlama Dili:** Python 3.8+
- **Web & Arayüz Geliştirme:** Streamlit, Plotly Interactive Charts
- **Doğal Dil İşleme (NLP):** TF-IDF Vectorizer, Cosine Similarity, Regex-based Stemmer & Cleaner
- **Belge Ayrıştırma:** PyMuPDF (`fitz`), `python-docx`
- **Makine Öğrenmesi:** Scikit-Learn (SVM, Random Forest, Naive Bayes, KNN, Lojistik Regresyon, K-Means, PCA, GridSearchCV, 5-Fold Cross Validation)
- **Veri Manipülasyonu & İstatistik:** Pandas, NumPy, SciPy
- **Veri Görselleştirme:** Matplotlib, Seaborn, Plotly Express & Graph Objects
- **Test & Kalite Güvencesi:** Pytest (25 unit & integration tests)
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
