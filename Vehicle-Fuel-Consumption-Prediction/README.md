# 🚗 Araçların Yakıt Tüketimi Tahmini (Auto MPG Fuel Consumption Prediction)

Bu proje, araçların teknik özelliklerini (silindir sayısı, motor hacmi, beygir gücü, ağırlık, ivmelenme, model yılı, menşei) kullanarak yakıt tüketimlerini (**MPG - Miles Per Gallon**) tahmin etmeyi amaçlayan kapsamlı bir Regresyon (**Regression**) ve Makine Öğrenmesi çalışmasıdır.

Projede **UCI Machine Learning Repository** üzerindeki Auto MPG veri seti kullanılmış; kayıp veri tamamlama (Imputation), aykırı değer temizleme (IQR), öznitelik mühendisliği (Log Transform / Skewness, One-Hot Encoding), düzenlileştirme modelleri (**Ridge, Lasso, ElasticNet**), **XGBoost** ve topluluk model birleştirme (**Averaging Models**) teknikleri uygulanmıştır.

---

## 📋 Proje Yapısı ve Mimari Akış

Proje mimarisi aşağıdaki işlem adımlarını sırasıyla takip eder:

```text
[1. Veri Yükleme & Problem Tanımı] ➔ [2. Kayıp Veri Tamamlama (Imputation)] ➔ [3. Keşifsel Veri Analizi (EDA)]
                                                                                      │
[6. Train-Test Split & Robust Scaling] ◄─ [5. Feature Engineering (Skewness & OHE)] ◄─ [4. Outlier Removal (IQR)]
             │
             ├─► [7. Doğrusal & Regularized Regresyon (Ridge, Lasso, ElasticNet)]
             ├─► [8. XGBoost Regressor]
             │
             └─► [9. Averaging Models (Ensemble)] ➔ Min MSE (Optimum Performance)
```

---

## 📊 Veri Seti Özellikleri (Dataset Description)

- **Kaynak:** Auto MPG Data Set (UCI Machine Learning Repository / Kaggle)
- **Örnek Sayısı (Samples):** 398 araç verisi (Aykırı değer temizliği sonrası ~395)
- **Özellikler (Features):**
  - `Cylinders`: Silindir sayısı (3, 4, 5, 6, 8)
  - `Displacement`: Motor hacmi
  - `Horsepower`: Beygir gücü (6 adet eksik veri içermekteydi, ortalama ile tamamlandı)
  - `Weight`: Araç ağırlığı (Pound)
  - `Acceleration`: 0-60 mph ivmelenme süresi (Saniye)
  - `Model Year`: Üretim yılı (1970 - 1982)
  - `Origin`: Üretim yeri / Menşei (1: Amerika, 2: Avrupa, 3: Japonya)
- **Hedef Değişken (Target):** `MPG` (Miles Per Gallon - Yakıt Tüketim Performansı)

---

## 🛠️ Kullanılan Teknolojiler ve Yöntemler

- **Programlama Dili:** Python 3.x
- **Veri Analizi & Görselleştirme:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy.stats`
- **Ölçeklendirme & Ön İşleme:** `RobustScaler`, `StandardScaler`, `get_dummies` (One-Hot Encoding), `np.log1p` (Skewness Düzeltme)
- **Regresyon & Topluluk Modelleri (`scikit-learn` & `xgboost`):**
  - `LinearRegression` (Temel Doğrusal Regresyon)
  - `Ridge` (L2 Regularization)
  - `Lasso` (L1 Regularization & Feature Selection)
  - `ElasticNet` (L1 + L2 Hybrid Regularization)
  - `XGBRegressor` (Extreme Gradient Boosting)
  - `AveragingModels` (Model Tahminlerinin Ortalamasını Alan Ensemble Yapı)
  - `GridSearchCV` (Çapraz Doğrulama ile Hiperparametre Optimizasyonu)

---

## ⚙️ Uygulanan Adımlar ve Yöntemler

### 1. Kayıp Veri Tamamlama (Missing Value Imputation)
- `Horsepower` sütununda tespit edilen 6 eksik veri, veri dağılımına zarar vermeyecek şekilde sütun ortalaması (`mean`) ile doldurulmuştur.

### 2. Aykırı Değer Tespiti ve Temizleme (Outlier Removal)
- Boxplot ve IQR (Interquartile Range) yöntemi kullanılarak `Horsepower` ve `Acceleration` değişkenlerindeki aşırı aykırı değerler eşik değer (`threshold = 2`) baz alınarak veri setinden çıkarılmıştır.

### 3. Öznitelik Mühendisliği (Feature Engineering)
- **Skewness (Çarpıklık) Düzeltme:** Pozitif çarpıklık gösteren bağımlı değişken `MPG` (`target`), `np.log1p` dönüşümü (Log Transformation) ile normal dağılıma yaklaştırılmıştır.
- **Categorical Encoding:** Kategorik yapıdaki `Cylinders` ve `Origin` değişkenleri `pd.get_dummies` kullanılarak One-Hot Encoding işlemine tabi tutulmuştur.

### 4. Ölçeklendirme (Scaling)
- Aykırı değerlere ve gürültüye karşı dayanıklılık sağlamak için `RobustScaler` tercih edilmiştir. (Karşılaştırma için `StandardScaler` da test edilmiştir).

---

## 📊 Modelleme ve Deney Sonuçları (MSE Performance)

Tüm modeller **Mean Squared Error (MSE)** metriği ile değerlendirilmiştir (Düşük MSE = Daha Yüksek Başarım):

| Model / Yöntem | StandardScaler MSE | RobustScaler MSE | Açıklama / Notlar |
| :--- | :---: | :---: | :--- |
| **Linear Regression** | 0.0206 | 0.0209 | Temel doğrusal model baseline. |
| **Ridge (L2)** | 0.0197 | 0.0188 | Katsayıları küçülterek overfitting'i azalttı. |
| **Lasso (L1)** | 0.0175 | 0.0165 | Önemsiz özellikleri sıfırlayarak öznitelik seçimi yaptı. |
| **ElasticNet** | 0.0174 | 0.0172 | L1 ve L2 penaltılarını dengeli birleştirdi. |
| **XGBoost Regressor** | 0.0171 | 0.0175 | Karmaşık, ağaç tabanlı güçlü boosting modeli. |
| **Averaging Models (Lasso + XGB)** | **0.0160** | **0.0156** | **En Düşük MSE!** İki güçlü modelin birleşimiyle en iyi sonuç elde edildi. |

---

## 🚀 Projenin Çalıştırılması

1. Bu depoyu klonlayın:
```bash
git clone https://github.com/kullanici_adi/auto-mpg-fuel-consumption-prediction.git
cd auto-mpg-fuel-consumption-prediction
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn xgboost
```

3. Python scriptini çalıştırın:
```bash
python main.py
```

---

##  Notlar

- **Scaling Karşılaştırması:** `RobustScaler` kullanımı, gürültülü verilerde `StandardScaler`'a göre Lasso ve Averaging Ensemble performansını gözle görülür şekilde artırmıştır.
- **Averaging Strategy:** Farklı yaklaşımlara sahip modellerin (Doğrusal L1 düzenlileştirmeli Lasso + Ağaç tabanlı boosting XGBoost) tahmin ortalaması alınarak tekil modellerin hataları sönümlenmiş ve en düşük MSE skoruna ulaşılmıştır.
