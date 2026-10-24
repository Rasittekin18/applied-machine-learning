# 🚀 Space Mission Data Analysis (1957 - Present)

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📌 Proje Hakkında
Bu proje, 1957 yılından (Sputnik 1'in fırlatılışından) günümüze kadar gerçekleştirilen tüm uzay görevlerinin verilerini detaylı bir şekilde inceleyen kapsamlı bir **Keşifçi Veri Analizi (Exploratory Data Analysis - EDA)** çalışmasıdır. 

Soğuk Savaş dönemindeki "Uzay Yarışı"ndan günümüzün özel uzay şirketlerine (SpaceX, Rocket Lab vb.) kadar uzay araştırmalarının tarihsel gelişimini, maliyetlerini, başarı oranlarını ve ülkeler bazındaki dağılımını interaktif görselleştirmelerle sunmaktadır.

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

- **Python 3**
- **Data Manipulation:** `pandas`, `numpy`
- **Data Visualization:** `plotly` (Express & Graph Objects), `seaborn`, `matplotlib`
- **Geographic Data Mapping:** `iso3166`
- **Preprocessing:** `scikit-learn` (`LabelEncoder`)

---

## 📊 Veri Seti İçeriği

Veri seti (`Space_Corrected.csv`), tarih boyunca gerçekleştirilen 4.300'den fazla uzay fırlatışına ait bilgileri içerir:

| Sütun Adı | Açıklama |
| :--- | :--- |
| **Company Name** | Fırlatmayı gerçekleştiren şirket/kurum (örn. SpaceX, NASA, RVSN USSR) |
| **Location** | Fırlatmanın yapıldığı konum ve ülke |
| **Datum** | Fırlatma tarihi ve saati |
| **Detail** | Kullanılan roket adı ve görev detayları |
| **Status Rocket** | Roketin güncel durumu (`StatusActive` / `StatusRetired`) |
| **Rocket** | Görevin maliyeti (Milyon $ cinsinden) |
| **Status Mission** | Görevin başarı durumu (`Success`, `Failure`, `Partial Failure`, `Prelaunch Failure`) |

---

## 📈 Analiz Kapsamı ve Analiz Adımları

Notebook içerisinde gerçekleştirilen temel analiz başlıkları şunlardır:

1. **Şirket Bazlı Fırlatma Sayıları:** Şirketlerin tarih boyunca gerçekleştirdiği toplam fırlatma sayılarının karşılaştırılması.
2. **Roket Durum Analizi:** Aktif kullanılan roketler ile emekliye ayrılan roketlerin oranı (`Pie Chart`).
3. **Görev Başarı Oranları:** Fırlatmaların başarı/başarısızlık dağılımı.
4. **Maliyet Dağılımları:**
   - Roket durumuna göre bütçe dağılımı.
   - Görev sonucuna göre harcanan bütçe dağılımı.
   - Şirket bazında harcanan toplam bütçe analizi.
5. **Zaman Serisi Analizi:** Yıllara göre düzenlenen görev sayılarındaki değişim ve trendler.
6. **Coğrafi & Ülke Analizleri:**
   - Ülkelere göre görev başarı oranları (`Subplots`).
   - Ülke, Şirket ve Görev Durumu hiyerarşisi (`Sunburst Chart`).
   - Dünya Haritası Üzerinde Görev Dağılımı (`Choropleth World Map`).

---

## 💻 Kurulum ve Çalıştırma

Projeyi kendi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

```bash
# Repoyu klonlayın
git clone https://github.com/Rasittekin18/space-mission-data-analysis.git

# Proje dizinine gidin
cd space-mission-data-analysis

# Gerekli Python kütüphanelerini yükleyin
pip install numpy pandas seaborn matplotlib plotly iso3166 scikit-learn
```

Ardından Jupyter Notebook veya VS Code üzerinden `space-mission-data-analysis.ipynb` dosyasını çalıştırabilirsiniz.

---

## 📝 Öne Çıkan Bulgular

- **En Çok Fırlatma Yapan Kurum:** SSCB dönemine ait RVSN USSR, 1700'ün üzerinde fırlatma ile açık ara lider konumdadır.
- **En Çok Bütçe Harcayan Kurum:** NASA, toplamda 76 Milyar $'dan fazla harcama ile ilk sırada yer almaktadır.
- **Zaman Analizi:** 1970'lerdeki Uzay Yarışı döneminde fırlatma sayıları zirve yapmış (1971'de 119 fırlatma), 2010 sonrasında ise özel sektörün katılımıyla tekrar büyük bir ivme kazanmıştır.

---


