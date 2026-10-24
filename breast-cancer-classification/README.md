# 🩺 Göğüs Kanseri Sınıflandırması (Breast Cancer Classification)

Bu proje, **Wisconsin Diagnostic Breast Cancer (WDBC)** veri setini kullanarak göğüs kanserinin **Malignant (Kötü Huylu - 1)** veya **Benign (İyi Huylu - 0)** olarak sınıflandırılmasını amaçlayan kapsamlı bir Makine Öğrenmesi çalışmasıdır.

Proje kapsamında veri keşfi (EDA), aykırı değer tespiti (Local Outlier Factor), verinin standardize edilmesi, K-En Yakın Komşu (KNN) algoritması, boyut indirgeme yöntemleri olan **Principal Component Analysis (PCA)** ve **Neighborhood Components Analysis (NCA)** ile model başarım artırma süreçleri adım adım uygulanmıştır.

---

## 📋 Proje Yapısı ve Akış Şeması

Proje mimarisi aşağıdaki işlem adımlarını sırasıyla takip eder:

```text
[1. Veri Seti & Problem Tanımı] ➔ [2. Kütüphaneler & Yükleme] ➔ [3. Keşifsel Veri Analizi (EDA)]
                                                                        │
[6. En İyi KNN Parametreleri] ◄─ [5. Standardizasyon] ◄─ [4. LOF Outlier Tespiti & Temizlik]
             │
             ├─► [7. PCA (Boyut İndirgeme - 2D) & KNN] ➔ %92.35 Başarım
             │
             └─► [8. NCA (Boyut İndirgeme - 2D) & KNN] ➔ %99.41 Başarım (Optimum)
```

---

## 📊 Veri Seti Özellikleri (Dataset Description)

- **Kaynak:** Breast Cancer Wisconsin (Diagnostic) Data Set (Kaggle / UCI Machine Learning Repository)
- **Örnek Sayısı (Samples):** 569 hasta verisi
- **Özellik Sayısı (Features):** 30 adet nümerik özellik (Hücre çekirdeği görüntülerinden elde edilmiş yarıçap, doku, çevre, alan, pürüzsüzlük vb. istatistikler)
- **Hedef Değişken (Target):**
  - `0`: Benign (İyi Huylu) — %62.7 (357 örnek)
  - `1`: Malignant (Kötü Huylu) — %37.3 (212 örnek)
- **Eksik Veri (Missing Values):** Yoktur.

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

- **Programlama Dili:** Python 3.x
- **Veri Analizi & İşleme:** `pandas`, `numpy`
- **Görselleştirme:** `matplotlib`, `seaborn`
- **Makine Öğrenmesi & Modelleme (`scikit-learn`):**
  - `StandardScaler` (Veri Standardizasyonu)
  - `LocalOutlierFactor` (LOF - Aykırı Değer Tespiti)
  - `train_test_split`, `GridSearchCV` (Model Seçimi & Hiperparametre Optimizasyonu)
  - `KNeighborsClassifier` (KNN Sınıflandırıcı)
  - `PCA` (Temel Bileşen Analizi - Gözetimsiz Boyut İndirgeme)
  - `NeighborhoodComponentsAnalysis` (NCA - Gözetimli Boyut İndirgeme)
  - `accuracy_score`, `confusion_matrix` (Model Değerlendirme)

---

## ⚙️ Uygulanan Adımlar ve Yöntemler

### 1. Keşifsel Veri Analizi (EDA) & Ön İşleme
- Gereksiz sütunlar (`id`, `Unnamed: 32`) veri setinden çıkarıldı.
- `diagnosis` sütunu `target` olarak yeniden adlandırıldı ve `M -> 1`, `B -> 0` şeklinde binary formata dönüştürüldü.
- Özellikler arasındaki korelasyon matrisi (`sns.clustermap`) hesaplandı. Target ile yüksek korelasyon gösteren özellikler filtrelendi (`threshold > 0.5`).
- Özelliklerin dağılımları ve ölçek farkları `sns.boxplot` ve `sns.pairplot` ile incelendi.

### 2. Aykırı Değer Tespiti (Outlier Detection - LOF)
- Yoğunluk tabanlı aykırı değer tespiti için **Local Outlier Factor (LOF)** algoritması kullanıldı.
- Belirlenen negatif outlier skor eşiğine (`threshold = -2.5`) göre tespit edilen aykırı değerler veri setinden temizlendi.

### 3. Veri Bölme & Standardizasyon
- Veri seti `%70 Eğitim (Train)` ve `%30 Test` olacak şekilde ayrıldı (`random_state=42`).
- Özellikler arasındaki ölçek farklarını gidermek için `StandardScaler` uygulandı. Scaler **sadece train verisi ile fit** edilerek test verisine sızıntı (data leakage) engellendi.

### 4. Modelleme ve Deney Sonuçları

| Model / Yöntem | Uygulanan Teknik | Test Başarımı (Accuracy) | Genel Değerlendirme |
| :--- | :--- | :---: | :--- |
| **Basic KNN** | $k=2$ (Varsayılan) | **~%95.30** | Başlangıç baseline modeli. |
| **Tuned KNN (GridSearchCV)** | Hiperparametre Optimizasyonu ($k=4$, `weights='distance'`) | **~%94.10** | Aşırı öğrenmeyi (overfitting) engelleyen dengeli model. |
| **PCA + Tuned KNN** | 30 Boyut $
ightarrow$ 2 Boyuta İndirgeme (Gözetimsiz) | **~%92.35** | Veriyi 2D görselleştirme imkanı sağladı; boyut indirgeme bilgi kaybına yol açtı. |
| **NCA + Tuned KNN** | 30 Boyut $
ightarrow$ 2 Boyuta İndirgeme (Gözetimli) | **~%99.41** | **En Yüksek Başarım!** Sınıf etiketlerini dikkate alarak ayrıştırılabilirliği maksimize etti. |

---

## 🚀 Projenin Çalıştırılması

1. Depoyu klonlayın:
```bash
git clone https://github.com/kullanici_adi/breast-cancer-classification-knn-nca.git
cd breast-cancer-classification-knn-nca
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

3. Veri setini (`cancer.csv`) proje dizinine ekleyin ve scripti çalıştırın:
```bash
python main.py
```

---

##  Notlar
- **Outlier Eşiği Değişimi:** LOF threshold değeri `-2.5` yerine farklı değerler seçilerek veri kümesindeki temizleme oranının başarım üzerindeki etkisi gözlemlenebilir.
- **PCA vs NCA Karşılaştırması:** PCA gözetimsiz (unsupervised) bir yöntem olduğu için varyansı korumaya odaklanır ancak sınıfları ayırma garantisi vermez. NCA ise gözetimli (supervised) çalışarak doğrusal dönüşüm ile sınıf ayrıştırılabilirliğini (class separability) maksimize eder ve KNN performansını zirveye taşır.
