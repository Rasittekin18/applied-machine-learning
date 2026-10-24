# ❤️ Heart Attack Analysis & Prediction

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📌 Proje Hakkında
Bu proje, hastaların klinik ve demografik verilerine dayanarak **kalp krizi riskini** analiz eden ve tahmin eden kapsamlı bir **Keşifçi Veri Analizi (EDA)** ve **Makine Öğrenmesi Sınıflandırma** çalışmasıdır.

Kalp krizi (miyokard enfarktüsü), kalp kasının bir bölümünün yeterli kan alamaması sonucu meydana gelir. Kan akışını geri kazandırmak için tedaviye ne kadar geç başlanırsa, kalp kasındaki hasar o kadar büyük olur. Koroner arter hastalığı (CAD), kalp krizinin başlıca nedenidir. Bu proje, hasta verilerini keşfederek Lojistik Regresyon modeli ile kalp krizi riskini tahmin etmeyi amaçlamaktadır.

---

## 🎯 Bu Projeden Neler Öğreneceksiniz?

- **Keşifçi Veri Analizi (EDA)**
- **Eksik Değer Analizi**
- **Kategorik ve Sayısal Özelliklerin Ayrıştırılması**
- **Standardizasyon (Standardization)**
- **Box - Swarm - Cat - Correlation Plot Analizleri**
- **Aykırı Değer (Outlier) Tespiti**
- **Makine Öğrenmesi Modelleme ve Hiperparametre Optimizasyonu**

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

- **Python 3**
- **Data Manipulation:** `pandas`, `numpy`
- **Data Visualization:** `seaborn`, `matplotlib`
- **Machine Learning:** `scikit-learn`
  - `StandardScaler`
  - `LogisticRegression`
  - `train_test_split`, `GridSearchCV`
  - `accuracy_score`, `roc_curve`

---

## 📊 Veri Seti İçeriği

Veri seti (`heart.csv`), hastaların klinik ölçümlerini ve kalp krizi risk durumunu içerir:

| Sütun Adı | Açıklama |
| :--- | :--- |
| **age** | Hastanın yaşı |
| **sex** | Hastanın cinsiyeti |
| **cp** | Göğüs ağrısı tipi (1: tipik anjina, 2: atipik anjina, 3: anjina olmayan ağrı, 4: asemptomatik) |
| **trtbps** | İstirahat halindeki kan basıncı (mm Hg) |
| **chol** | Kolesterol seviyesi (mg/dl) |
| **fbs** | Açlık kan şekeri > 120 mg/dl (1: evet, 0: hayır) |
| **restecg** | İstirahat elektrokardiyografi sonuçları (0: normal, 1: ST-T dalga anormalliği, 2: sol ventrikül hipertrofisi) |
| **thalachh** | Ulaşılan maksimum kalp atış hızı |
| **exng** | Egzersize bağlı anjina (1: evet, 0: hayır) |
| **caa** | Büyük damar sayısı (0-3) |
| **output** | Hedef değişken — kalp krizi riski (0: düşük risk, 1: yüksek risk) |

---

## 📈 Analiz Kapsamı ve Analiz Adımları

Notebook içerisinde gerçekleştirilen temel analiz ve modelleme adımları şunlardır:

1. **Python Kütüphaneleri:** Kullanılan kütüphanelerin içe aktarılması.
2. **Veri İçeriği:** Veri setindeki sütunların ve klinik anlamlarının açıklanması.
3. **Veri Okuma ve İnceleme:** `head()`, `describe()`, `info()` ile temel istatistiksel inceleme.
4. **Eksik Değer Analizi:** `isnull().sum()` ile eksik veri kontrolü.
5. **Benzersiz Değer Analizi:** Her sütundaki farklı değer sayısının incelenmesi.
6. **Kategorik Özellik Analizi:** `countplot` ile hedef değişkene göre dağılım.
7. **Sayısal Özellik Analizi:** `pairplot` ile ikili ilişkilerin incelenmesi.
8. **Standardizasyon:** `StandardScaler` ile sayısal özelliklerin ölçeklendirilmesi.
9. **Box Plot Analizi:** Ölçeklenmiş özelliklerin hedef değişkene göre dağılımı.
10. **Swarm Plot Analizi:** Özelliklerin detaylı dağılım görselleştirmesi.
11. **Cat Plot Analizi:** Cinsiyet ve egzersiz anjinine göre yaş dağılımı.
12. **Korelasyon Analizi:** `heatmap` ile değişkenler arası ilişkiler.
13. **Aykırı Değer Tespiti:** IQR (Çeyrekler Arası Aralık) yöntemi ile outlier tespiti.
14. **Modelleme:**
    - Kategorik sütunların encode edilmesi (`get_dummies`)
    - Ölçeklendirme (`StandardScaler`)
    - Train/Test ayrımı (%90 - %10)
    - Lojistik Regresyon modeli eğitimi ve ROC eğrisi ile değerlendirme
    - `GridSearchCV` ile hiperparametre optimizasyonu (penalty: l1/l2)

---

## 💻 Kurulum ve Çalıştırma

Projeyi kendi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

```bash
# Repoyu klonlayın
git clone https://github.com/Rasittekin18/heart-attack-analysis-prediction.git

# Proje dizinine gidin
cd heart-attack-analysis-prediction

# Gerekli Python kütüphanelerini yükleyin
pip install numpy pandas seaborn matplotlib scikit-learn
```

Ardından Jupyter Notebook veya VS Code üzerinden `heart-attack-analysis-prediction.ipynb` dosyasını çalıştırabilirsiniz.

> **Not:** Notebook, orijinal haliyle Kaggle ortamındaki `/kaggle/input/heart-attack-analysis-prediction-dataset/heart.csv` yolunu referans almaktadır. Yerel ortamda çalıştırmak için veri setini Kaggle üzerinden indirip dosya yolunu kendi ortamınıza göre güncellemeniz gerekmektedir.

---

## 📝 Öne Çıkan Bulgular

- **Aykırı Değerler:** `age`, `trtbps`, `chol`, `thalachh` ve `oldpeak` sütunlarında IQR yöntemiyle aykırı değerler tespit edilmiştir.
- **Değişkenler Arası İlişki:** Göğüs ağrısı tipi (`cp`) ve maksimum kalp atış hızı (`thalachh`) gibi değişkenler, kalp krizi riskiyle belirgin ilişki göstermektedir.
- **Model Performansı:** Lojistik Regresyon modeli, test verisinde tatmin edici bir doğruluk (accuracy) skoru elde etmiştir; ROC eğrisi ile modelin ayırt edicilik gücü değerlendirilmiştir.
- **Hiperparametre Optimizasyonu:** `GridSearchCV` ile en iyi `penalty` parametresi (l1/l2) belirlenerek model ince ayarı yapılmıştır.

---
