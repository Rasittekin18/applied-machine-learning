# 😊 World Happiness Report - Exploratory Data Analysis

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📌 Proje Hakkında
Bu proje, **Dünya Mutluluk Raporu (World Happiness Report)** verileri üzerine yapılan kapsamlı bir **Keşifçi Veri Analizi (Exploratory Data Analysis - EDA)** çalışmasıdır.

World Happiness Report, küresel mutluluğun durumunu inceleyen önemli bir araştırmadır. Hükümetler, kuruluşlar ve sivil toplum, politika oluşturma kararlarını bilgilendirmek için giderek daha fazla mutluluk göstergelerini kullanmaktadır. Ekonomi, psikoloji, anket analizi, ulusal istatistikler, sağlık ve kamu politikası alanlarındaki uzmanlar, refah ölçümlerinin ülkelerin ilerlemesini değerlendirmede nasıl etkin bir şekilde kullanılabileceğini ortaya koymaktadır.

---

## 🎯 Bu Projeden Neler Öğreneceksiniz?

- **İki Değişkenli (Bivariate) Veri Analizi**
- **Çok Değişkenli (Multivariate) Veri Analizi**
- **Seaborn** görselleştirme teknikleri: `bar`, `box`, `kde`, `swarm`, `heatmap`, `clustermap`
- **Plotly** görselleştirme teknikleri: animasyonlu grafikler ve dünya haritası (`choropleth`)

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

- **Python 3**
- **Data Manipulation:** `pandas`, `numpy`
- **Data Visualization:** `seaborn`, `matplotlib`, `plotly.express`
- **Environment:** Jupyter Notebook / Kaggle Kernel

---

## 📊 Veri Seti İçeriği

Proje üç ayrı veri setini bir araya getirmektedir:

| Dosya | Açıklama |
| :--- | :--- |
| `world-happiness-report.csv` | 2005-2020 yılları arasını kapsayan, ülkelerin yıl bazında mutluluk skorlarını içeren zaman serisi verisi |
| `world-happiness-report-2021.csv` | 2021 yılına ait güncel mutluluk skorları ve bölgesel göstergeler |
| `population_total_long.csv` | 1960-2018 arası ülke nüfus verileri (animasyonlu grafiklerde balon boyutu için kullanılmıştır) |

**Öne çıkan sütunlar:**

| Sütun Adı | Açıklama |
| :--- | :--- |
| **Ladder score / Life Ladder** | Mutluluk skoru (öznel iyi oluş / life evaluation) |
| **Logged GDP per capita** | Kişi başına düşen GSYİH (logaritmik) |
| **Social support** | Sosyal destek algısı |
| **Healthy life expectancy** | Sağlıklı yaşam beklentisi |
| **Freedom to make life choices** | Yaşam seçimlerinde özgürlük algısı |
| **Generosity** | Cömertlik endeksi |
| **Perceptions of corruption** | Yolsuzluk algısı |
| **Regional indicator** | Ülkenin ait olduğu bölge |

---

## 📈 Analiz Kapsamı ve Analiz Adımları

Notebook içerisinde gerçekleştirilen temel analiz başlıkları şunlardır:

1. **Python Kütüphaneleri:** Kullanılan kütüphanelerin içe aktarılması.
2. **Veri İçeriği:** Veri setindeki sütunların ve metodolojinin açıklanması.
3. **Veri Okuma ve İnceleme:** `head()`, `describe()`, `info()` ile temel istatistiksel inceleme.
4. **2021 Yılı Veri Dağılımları:** Benzersiz ülkeler, bölgesel gösterge sayıları ve özellik dağılımları (`boxplot`).
5. **2021'in En Mutlu ve En Mutsuz Ülkeleri:** `barplot` ile karşılaştırma.
6. **Bölgesel Göstergeye Göre Mutluluk Skoru Dağılımı:** `kdeplot` ile yoğunluk analizi.
7. **Harita Üzerinde Mutluluk Skoru Dağılımı:** Yıllara göre animasyonlu `choropleth` dünya haritası.
8. **2021'in En Cömert ve En Az Cömert Ülkeleri:** `barplot` ile karşılaştırma.
9. **Harita Üzerinde Cömertlik Dağılımı:** Animasyonlu `choropleth` dünya haritası.
10. **Bölgesel Göstergeye Göre Cömertlik Dağılımı:** `swarmplot` ile analiz.
11. **Mutluluk ve Gelir İlişkisi:** Nüfus verisiyle zenginleştirilmiş, yıllara göre animasyonlu `scatter` grafiği.
12. **Mutluluk ve Özgürlük İlişkisi:** Animasyonlu `scatter` grafiği.
13. **Mutluluk ve Yolsuzluk Algısı İlişkisi:** Bölgeye göre renklendirilmiş, animasyonlu `scatter` grafiği.
14. **Değişkenler Arası İlişkiler:** `heatmap` ve `clustermap` ile korelasyon analizi.

---

## 💻 Kurulum ve Çalıştırma

Projeyi kendi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

```bash
# Repoyu klonlayın
git clone https://github.com/Rasittekin18/world-happiness-eda.git

# Proje dizinine gidin
cd world-happiness-eda

# Gerekli Python kütüphanelerini yükleyin
pip install numpy pandas seaborn matplotlib plotly
```

Ardından Jupyter Notebook veya VS Code üzerinden `world-happiness-eda.ipynb` dosyasını çalıştırabilirsiniz.

> **Not:** Notebook, orijinal haliyle Kaggle ortamındaki `/kaggle/input/...` yollarını referans almaktadır. Yerel ortamda çalıştırmak için ilgili veri setlerini (World Happiness Report 2021 ve World Population 1960-2018) Kaggle üzerinden indirip dosya yollarını kendi ortamınıza göre güncellemeniz gerekmektedir.

---

## 📝 Öne Çıkan Bulgular

- **Bölgesel Farklar:** Mutluluk skoru dağılımı bölgeden bölgeye belirgin şekilde farklılık göstermektedir; bazı bölgeler ortalamanın oldukça üzerinde, bazıları ise oldukça altında kümelenmektedir.
- **Gelir - Mutluluk İlişkisi:** Kişi başına düşen GSYİH ile mutluluk skoru arasında yıllar içinde tutarlı bir pozitif ilişki gözlemlenmektedir.
- **Özgürlük ve Yolsuzluk Algısı:** Yaşam seçimlerinde özgürlük algısı mutlulukla pozitif; yolsuzluk algısı ise genellikle negatif yönde ilişkilidir.
- **Değişkenler Arası Korelasyon:** Sosyal destek, sağlıklı yaşam beklentisi ve GSYİH, mutluluk skoruyla en güçlü korelasyona sahip değişkenler arasında yer almaktadır.

---

