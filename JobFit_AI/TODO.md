# 📋 JobFit AI: Proje İlerleme ve Takip Listesi (TODO)

> **JobFit AI**: Akıllı CV & İş İlanı Uygunluk Analizörü ve Beceri Tavsiye Motoru  
> Bu belge, projenin tüm klasörlerini, dosyalarını ve geliştirme aşamalarını adım adım takip etmek için hazırlanmıştır.

---

## 📂 Proje Klasör ve Dosya Haritası

```text
JobFit_AI/
│
├── 📄 TODO.md                      # [x] Canlı Proje Takip ve Durum Belgesi
├── 📄 requirements.txt             # [x] Python kütüphane bağımlılıkları
├── 📄 README.md                    # [x] GitHub vitrini, rozetler ve çalıştırma rehberi
├── 📄 app.py                       # [x] Streamlit tabanlı modern web arayüzü
│
├── 📁 data/                        # Veri Setleri ve Bilgi Tabanı
│   ├── 📄 skills_dictionary.json   # [x] 100+ teknik beceri kütüphanesi (Data Science, Backend, Frontend, DevOps)
│   ├── 📄 generate_dataset.py      # [x] Sentetik iş ilanı veri seti üretici script
│   └── 📄 job_postings.csv         # [x] 720 adet etiketli iş ilanı veri seti
│
├── 📁 src/                         # Makine Öğrenmesi ve Çekirdek Kodlar
│   ├── 📄 __init__.py              # [x] Paket başlatıcı
│   ├── 📄 nlp_preprocessor.py      # [x] NLP metin temizleme, tokenization ve TF-IDF (Bölüm 18)
│   ├── 📄 recommender.py           # [x] Kosinüs benzerliği ve Beceri Açığı (Skill Gap) motoru (Bölüm 21)
│   ├── 📄 classifier.py            # [x] Rol ve Kıdem sınıflandırıcıları: KNN, SVM, Random Forest (Bölüm 10, 11, 14)
│   ├── 📄 model_evaluator.py       # [x] Model değerlendirme, Confusion Matrix ve F1 analizi (Bölüm 15)
│   └── 📄 cv_parser.py             # [x] PDF, DOCX ve düz metin CV okuma yardımcısı
│
└── 📁 models/                      # Eğitilmiş Model Ağırlıkları (.joblib)
    ├── 📄 tfidf_vectorizer.joblib  # [x] Eğitilmiş TF-IDF kelime vektörleştiricisi
    ├── 📄 role_classifier.joblib   # [x] Pozisyon sınıflandırıcı model (Random Forest / SVM)
    ├── 📄 level_classifier.joblib  # [x] Kıdem seviyesi tahmin edici model
    └── 📄 benchmark_summary.joblib # [x] Model kıyaslama ve Confusion Matrix verileri
```

---

## 🎯 Aşamalı Geliştirme Durumu (Milestones)

### [x] Faz 1: Veri ve Bilgi Tabanının Hazırlanması
- [x] `JobFit_AI/data/skills_dictionary.json`: Data Science, Backend, Frontend, DevOps ve Genel yetkinlikleri içeren zengin beceri sözlüğü oluşturuldu.
- [x] `JobFit_AI/data/generate_dataset.py`: 4 rol ve 3 kıdem seviyesine göre gerçekçi iş ilanları üreten script hazırlandı.
- [x] `JobFit_AI/data/job_postings.csv`: 720 satırlık etiketli eğitim veri seti başarıyla üretildi.

---

### [x] Faz 2: NLP ve Metin Ön İşleme Pipeline'ı (Kurs Bölüm 18)
- [x] `src/nlp_preprocessor.py`:
  - [x] Regex ile URL, e-posta, telefon ve alfasayısal olmayan karakterleri temizleme.
  - [x] Küçük harfe dönüştürme ve noktalama işaretlerini ayıklama.
  - [x] Standart İngilizce ve mesleki stop-words (etkisiz kelimeler) temizliği.
  - [x] Kelime köklerini yakalamak için hafif/güvenilir kök bulma (Stemming) mantığı.
  - [x] `TfidfVectorizer` (ngram_range=(1, 2), max_features=3000) entegrasyonu.
  - [x] Birim test ile metin ön işlemenin başarıyla doğrulanması.

---

### [x] Faz 3: Öneri Sistemi & Beceri Eşleştirme Motoru (Kurs Bölüm 21)
- [x] `src/recommender.py`:
  - [x] CV vektörü ile İş İlanı vektörü arasında **Kosinüs Benzerliği (Cosine Similarity)** formülü.
  - [x] Beceri Çıkarıcı (Skill Extractor): Metin içerisinden `skills_dictionary.json` ile eşleşen teknik terimleri ayıklama.
  - [x] Beceri Açığı Analizi (Skill Gap Analysis): İlanda istenip adayın CV'sinde eksik olan kritik teknolojileri listeleme.
  - [x] Akıllı Tavsiye Üretici: Kişiselleştirilmiş ATS ve kariyer optimizasyon tavsiyeleri.

---

### [x] Faz 4: Makine Öğrenmesi Sınıflandırma ve Kıyaslama (Kurs Bölüm 10, 11, 14, 15, 20)
- [x] `src/classifier.py`:
  - [x] **Naive Bayes (MultinomialNB)** modeli (Bölüm 12).
  - [x] **K-Nearest Neighbors (KNN)** modeli (Bölüm 10).
  - [x] **Support Vector Machine (SVM / SVC)** modeli (Bölüm 11).
  - [x] **Random Forest Classifier** modeli (Bölüm 14).
  - [x] 5-Katlı Çapraz Doğrulama (K-Fold CV) ile model kararlılığı ölçümü (Bölüm 20).
  - [x] Kıdem Seviyesi (Junior, Mid, Senior) sınıflandırıcı modeli.
  - [x] Eğitilmiş ağırlıkların `models/` klasörüne `.joblib` olarak kaydedilmesi.
- [x] `src/model_evaluator.py`:
  - [x] Confusion Matrix (Karmaşıklık Matrisi) ısı haritası görselleştirmesi (Bölüm 15).
  - [x] Modellerin Test ve CV Doğruluklarını kıyaslayan karşılaştırma tablosu ve sütun grafiği.

---

### [x] Faz 5: CV Dosya Okuyucu (Parser)
- [x] `src/cv_parser.py`:
  - [x] PDF formatındaki CV'leri metne dönüştürme (`pymupdf / fitz`).
  - [x] DOCX formatındaki CV'leri metne dönüştürme (`python-docx`).
  - [x] Düz metin (TXT / Kopyala-Yapıştır) girdilerini normalize etme.

---

### [x] Faz 6: Modern Streamlit Web Arayüzü (`app.py`)
- [x] `app.py`:
  - [x] **Ana Panel (Dashboard):** Sol tarafta CV girişi (PDF/DOCX/TXT yükleme veya yapıştırma), sağ tarafta İş İlanı girişi.
  - [x] **Metrik Kartları:** Anlık Uyum Skoru (%0-%100), Semantik Skor, Beceri Skoru, Eşleşen Beceri Sayısı.
  - [x] **Eksik Beceriler ve Eylem Planı Kartı:** Yeşil, kırmızı ve gri renkli rozetlerle (badges) görsel analiz.
  - [x] **Model Laboratuvarı Sekmesi:** Kurstaki 4 algoritmanın başarı tablosu ve interaktif Confusion Matrix grafikleri.

---

### [x] Faz 7: GitHub Vitrini ve Dokümantasyon
- [x] `requirements.txt`: Gerekli tüm kütüphanelerin listesi eksiksiz tanımlandı.
- [x] `README.md`: Profesyonel Shields.io rozetleri, mimari akış diyagramı, kurulum rehberi ve kuramsal makine öğrenmesi açıklamaları eklendi.

---

## 📊 İlerleme Özeti

| Faz | Açıklama | Durum |
|:---:|:---|:---:|
| **Faz 1** | Veri Seti ve Beceri Sözlüğü | ✅ Tamamlandı (100%) |
| **Faz 2** | NLP & Metin Ön İşleme Motoru | ✅ Tamamlandı (100%) |
| **Faz 3** | Öneri Sistemi & Skill Gap Analizi | ✅ Tamamlandı (100%) |
| **Faz 4** | ML Sınıflandırıcılar & Kıyaslama | ✅ Tamamlandı (100%) |
| **Faz 5** | CV Okuyucu (PDF / DOCX / Text) | ✅ Tamamlandı (100%) |
| **Faz 6** | Streamlit Web Uygulaması | ✅ Tamamlandı (100%) |
| **Faz 7** | GitHub Dokümantasyonu & README | ✅ Tamamlandı (100%) |
