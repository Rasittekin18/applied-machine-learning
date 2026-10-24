# 🌲 Ensemble Learning (Topluluk Öğrenmesi) & Karşılaştırmalı Sınıflandırma

Bu proje, Makine Öğrenmesinde temel sınıflandırıcılar (**Basic Classifiers**) ile topluluk öğrenmesi (**Ensemble Learning**) yöntemlerinin sentetik veri setleri üzerindeki performanslarını, karar sınırlarını (decision boundaries) ve başarım skorlarını karşılaştırmalı olarak incelemektedir.

Projede **scikit-learn** kütüphanesi kullanılarak 3 farklı sentetik veri seti oluşturulmuş; temel modeller (KNN, SVM, Decision Tree) ile Bagging (Random Forest), Boosting (AdaBoost) ve Voting (Çoğunluk Oylaması) topluluk teknikleri test edilmiştir.

---

## 📋 Proje Yapısı ve Mimari Akış

```text
[1. Sentetik Veri Üretimi] ➔ [2. Robust Standardizasyon] ➔ [3. Train-Test Split (%60 / %40)]
  (Moons, Circles, Classify)           │
                                       ▼
                       ┌───────────────────────────────┐
                       │      Model Karşılaştırma      │
                       └───────────────┬───────────────┘
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            ▼                                                     ▼
  [Temel Sınıflandırıcılar]                             [Topluluk Öğrenmesi (Ensemble)]
  • SVM (RBF Kernel)                                    • Random Forest (Bagging)
  • KNN (k=15)                                          • AdaBoost (Boosting w/ Decision Stump)
  • Decision Tree (max_depth=2)                         • Voting Classifier (Hard Voting)
            │                                                     │
            └──────────────────────────┬──────────────────────────┘
                                       ▼
                     [4. 2D Karar Sınırları & Skor Analizi]
```

---

## 📊 Sentetik Veri Setleri (Datasets)

Proje kapsamında `sklearn.datasets` ile üretilen 3 farklı veri mimarisi kullanılmıştır:

1. **Make Moons (`Moons`):**
   - İki boyutlu, iç içe geçmiş iki hilal (moon) şeklinde non-linear dağılım.
   - **Görselleştirme:** 2D Karar Sınırları çizdirilmektedir.
   - **Parametreler:** `n_samples=2000`, `noise=0.3`

2. **Make Circles (`Circles`):**
   - İki boyutlu, iç içe dairesel halkalar halinde non-linear ayrışan yapı.
   - **Görselleştirme:** 2D Karar Sınırları çizdirilmektedir.
   - **Parametreler:** `n_samples=2000`, `factor=0.1`, `noise=0.3`

3. **Make Classification (`Multi-Feature / High-Dim`):**
   - Çok boyutlu ve daha yüksek karmaşıklığa sahip genel sınıflandırma veri seti.
   - **Görselleştirme:** Yüksek boyutlu olduğu için sadece teorik başarım ölçülmektedir.
   - **Parametreler:** `n_samples=2000`, `n_features=10`, `n_classes=2`, `flip_y=0.3` (gürültü/noise)

---

## 🛠️ Kullanılan Teknolojiler ve Yöntemler

- **Programlama Dili:** Python 3.x
- **Veri Analizi & İşleme:** `pandas`, `numpy`
- **Görselleştirme:** `matplotlib`, `seaborn`
- **Ölçeklendirme:** `RobustScaler` (Aykırı değerlere karşı dayanıklı ölçekleme)
- **Modelleme & Topluluk Yöntemleri (`scikit-learn`):**
  - **SVC (RBF Kernel):** Destek Vektör Sınıflandırıcısı.
  - **KNeighborsClassifier (KNN):** Komşuluk tabanlı sınıflandırıcı ($k=15$).
  - **DecisionTreeClassifier:** Karar Ağacı ($max\_depth=2$).
  - **RandomForestClassifier (Bagging):** Bootstrap örnekleme ile 10 adet karar ağacının birleşimi ($n\_estimators=10$).
  - **AdaBoostClassifier (Boosting):** Zayıf öğrenicileri (Decision Stump) ağırlıklandırarak ardışık eğiten boosting modeli.
  - **VotingClassifier (Ensemble Combo):** Tüm modellerin tahminlerini oy çokluğuyla (Hard Voting) birleştiren kolektif hibrit yapı.

---

## ⚙️ Model Performansları ve Karşılaştırma Tablosu

| Model / Yöntem | Tür | Moons Test Score | Circles Test Score | Classification (10D) Test Score |
| :--- | :--- | :---: | :---: | :---: |
| **SVC (RBF)** | Basic | **~%91.0** | **~%88.5** | **~%84.2** |
| **KNN (k=15)** | Basic | **~%91.0** | **~%88.5** | **~%80.0** |
| **Decision Tree** | Basic | **~%89.5** | **~%88.0** | **~%80.8** |
| **Random Forest** | Bagging | **~%90.5** | **~%88.5** | **~%81.5** |
| **AdaBoost** | Boosting | **~%90.2** | **~%87.0** | **~%81.2** |
| **Voting Classifier**| Ensemble Combo | **~%91.2** | **~%88.8** | **~%83.8** |

*Not: Skorlar eklenen noise (%30) ve `random_state=42` parametre yapılandırmalarına göre elde edilen ortalama değerlerdir.*

---

## 🔬 Teorik Analiz ve Çıkarımlar

1. **Bagging vs Boosting:**
   - **Bagging (Random Forest):** Paralel ağaçlar eğiterek **varyansı (overfitting)** düşürür. Derinlik sınırlandığında ($max\_depth=2$) stabil sonuçlar verir.
   - **Boosting (AdaBoost):** Yanlış sınıflandırılan örneklere odaklanarak **yanlılığı (bias)** düşürmeyi amaçlar. Gürültülü verilerde hassastır.
2. **Voting Classifier Gücü:**
   - Farklı karakterdeki modellerin (RBF Kernel SVM, Mesafe tabanlı KNN, Kural tabanlı Ağaçlar) zayıf yönlerini birbirleriyle sönümleyerek genel başarım stabilitesini artırır.
3. **RobustScaler Önemi:**
   - Veriye gürültü (noise) eklendiğinde `StandardScaler` yerine medyan ve IQR tabanlı `RobustScaler` kullanılması model kararlılığını korumuştur.

---

## 🚀 Projenin Çalıştırılması

1. Bu depoyu klonlayın:
```bash
git clone https://github.com/kullanici_adi/ensemble-learning-classification.git
cd ensemble-learning-classification
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

3. Python scriptini çalıştırın:
```bash
python ensemble_learning.py
```

---

##  Notlar

- **Hiperparametre Deneyleri:** `n_estimators` değerini 10'dan 100'e çıkararak veya Decision Tree derinliğini (`max_depth`) değiştirerek Overfitting/Underfitting dengesini gözlemleyebilirsiniz.
- **Voting Yöntemi:** VotingClassifier parametresini `voting='hard'` yerine `voting='soft'` (olasılık tabanlı) olarak değiştirerek (uygun classifier'lar ile) performans farkını test edebilirsiniz.
