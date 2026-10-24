# 💧 Water Quality Explanatory Data Analysis & Classification

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📌 Proje Hakkında
Bu proje, su örneklerinin fiziksel ve kimyasal özelliklerine dayanarak **içilebilirliğini (potability)** analiz eden ve tahmin eden kapsamlı bir **Keşifçi Veri Analizi (EDA)** ve **Makine Öğrenmesi Sınıflandırma** çalışmasıdır.

Güvenli içme suyuna erişim, sağlık için temel bir insan hakkı ve etkili sağlık koruma politikalarının bir bileşenidir. Bu proje, su kalitesi parametrelerini keşfederek suyun içilebilir olup olmadığını Karar Ağacı ve Rastgele Orman (Random Forest) sınıflandırıcıları ile tahmin etmeyi amaçlamaktadır.

---

## 🎯 Bu Projeden Neler Öğreneceksiniz?

- **İki Değişkenli ve Çok Değişkenli Veri Analizi**
- **Korelasyon Analizi** (`clustermap`)
- **Ön İşleme:** Eksik değer analizi, train-test split ve normalizasyon
- **Modelleme:** Decision Tree ve Random Forest Sınıflandırıcıları
- **Karar Ağacının Görselleştirilmesi**
- **Random Forest Hiperparametre Optimizasyonu**

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

- **Python 3**
- **Data Manipulation:** `pandas`, `numpy`
- **Data Visualization:** `seaborn`, `matplotlib`, `plotly.express`
- **Missing Data Visualization:** `missingno`
- **Machine Learning:** `scikit-learn`
  - `DecisionTreeClassifier`
  - `RandomForestClassifier`
  - `RandomizedSearchCV`, `RepeatedStratifiedKFold`, `train_test_split`
  - `precision_score`, `confusion_matrix`

---

## 📊 Veri Seti İçeriği

Veri seti (`water_potability.csv`), su örneklerine ait 9 fiziksel/kimyasal özellik ile içilebilirlik etiketini içerir:

| Sütun Adı | Açıklama |
| :--- | :--- |
| **ph** | Suyun asit-baz dengesini gösteren pH değeri (WHO limiti: 6.5 - 8.5) |
| **Hardness** | Kalsiyum ve magnezyum tuzlarından kaynaklanan su sertliği |
| **Solids (TDS)** | Toplam çözünmüş katı madde miktarı (Desirable limit: 500 mg/l) |
| **Chloramines** | İçme suyunda kullanılan dezenfektan seviyesi (güvenli sınır: 4 mg/L) |
| **Sulfate** | Doğal olarak bulunan sülfat konsantrasyonu |
| **Conductivity** | Suyun elektriksel iletkenliği (WHO limiti: 400 μS/cm) |
| **Organic_carbon** | Sudaki organik bileşiklerdeki toplam karbon miktarı |
| **Trihalomethanes** | Klor ile arıtılan suda oluşabilen kimyasallar (güvenli sınır: 80 ppm) |
| **Turbidity** | Suyun bulanıklığı (WHO önerisi: 5.00 NTU altı) |
| **Potability** | Hedef değişken — suyun içilebilir olup olmadığı (1: İçilebilir, 0: İçilemez) |

---

## 📈 Analiz Kapsamı ve Analiz Adımları

Notebook içerisinde gerçekleştirilen temel analiz ve modelleme adımları şunlardır:

1. **Python Kütüphaneleri:** Kullanılan kütüphanelerin içe aktarılması.
2. **Veri İçeriği:** Her bir özelliğin sağlık ve WHO standartları açısından açıklanması.
3. **Veri Okuma ve İnceleme:** `head()`, `describe()`, `info()` ile temel istatistiksel inceleme.
4. **Bağımlı Değişken (Potability) Analizi:** İçilebilir/içilemez örneklerin oranı (`Pie Chart`).
5. **Özellikler Arası Korelasyon:** `clustermap` ile korelasyon analizi.
6. **Özelliklerin Dağılımı:** İçilebilir ve içilemez sınıflar için `kdeplot` karşılaştırmaları.
7. **Ön İşleme - Eksik Değer Problemi:** `missingno` ile görselleştirme ve ortalama ile doldurma.
8. **Ön İşleme - Train-Test Split ve Normalizasyon:** %70-%30 ayrım ve min-max normalizasyon.
9. **Modelleme:** Decision Tree ve Random Forest sınıflandırıcılarının eğitimi ve `precision_score` / `confusion_matrix` ile değerlendirilmesi.
10. **Karar Ağacının Görselleştirilmesi:** `tree.plot_tree` ile model yapısının incelenmesi.
11. **Random Forest Hiperparametre Optimizasyonu:** `RandomizedSearchCV` ve `RepeatedStratifiedKFold` ile en iyi parametre kombinasyonunun aranması.

---

## 💻 Kurulum ve Çalıştırma

Projeyi kendi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

```bash
# Repoyu klonlayın
git clone https://github.com/Rasittekin18/water-quality-analysis.git

# Proje dizinine gidin
cd water-quality-analysis

# Gerekli Python kütüphanelerini yükleyin
pip install numpy pandas seaborn matplotlib plotly missingno scikit-learn
```

Ardından Jupyter Notebook veya VS Code üzerinden `water-quality-analysis.ipynb` dosyasını çalıştırabilirsiniz.

> **Not:** Notebook, orijinal haliyle Kaggle ortamındaki `/kaggle/input/water-potability/water_potability.csv` yolunu referans almaktadır. Yerel ortamda çalıştırmak için veri setini [Kaggle - Water Potability](https://www.kaggle.com/datasets/adityakadiwal/water-potability) üzerinden indirip dosya yolunu kendi ortamınıza göre güncellemeniz gerekmektedir.

---

## 📝 Öne Çıkan Bulgular

- **Sınıf Dengesizliği:** Veri setindeki içilebilir (Potable) ve içilemez (Not Potable) örnek sayıları arasında belirgin bir dengesizlik bulunmaktadır.
- **Eksik Veriler:** `ph`, `Sulfate` ve `Trihalomethanes` sütunlarında eksik değerler tespit edilmiş ve ortalama değer ile doldurulmuştur.
- **Model Performansı:** Random Forest sınıflandırıcısı, Decision Tree'ye kıyasla genellikle daha yüksek `precision` skoru sunmaktadır.
- **Hiperparametre Optimizasyonu:** `RandomizedSearchCV` ile `n_estimators`, `max_features` ve `max_depth` parametreleri optimize edilerek model performansı iyileştirilmiştir.

---

