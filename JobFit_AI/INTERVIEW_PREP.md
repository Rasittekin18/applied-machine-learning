# 🎯 JobFit AI: Mülakat Hazırlık ve Teknik Savunma Rehberi

> Bu doküman, **JobFit AI** projesini özgeçmişinize eklediğinizde veya teknik mülakatlarda bu proje hakkında soru sorulduğunda, kullandığınız makine öğrenmesi kararlarını en üst düzeyde savunabilmeniz için hazırlanmıştır.

---

### Soru 1: CV ve İş İlanı eşleştirmesinde neden Öklid Mesafesi yerine Kosinüs Benzerliği (Cosine Similarity) kullandınız?

**Cevap:**
> *"Öklid mesafesi metinlerin uzunluğuna (büyüklüğüne) aşırı duyarlıdır. Örneğin, 1 sayfalık kısa bir CV ile 5 sayfalık detaylı bir CV aynı yetkinliklere sahip olsa bile, uzun CV'de kelime frekansları yüksek olacağı için Öklid mesafesi onları uzayda birbirinden çok uzak gösterecektir.*
>
> *Buna karşılık **Kosinüs Benzerliği**, iki vektörün mutlak büyüklüğüne değil, aralarındaki **açının kosinüsüne ($\cos \theta$)** odaklanır:*
> $$\text{Cosine Similarity} = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$$
> *Bu sayede belgenin ne kadar uzun veya kısa olduğundan bağımsız olarak, yalnızca konu yönelimini ve anlamsal örtüşmeyi objektif olarak ölçebiliriz."*

---

### Soru 2: Neden klasik Bag of Words (CountVectorizer) yerine TF-IDF kullandınız?

**Cevap:**
> *"Basit Bag of Words yalnızca kelime sayımlarını tutar. Bu yaklaşımda teknik bir metinde sıkça geçen dolgu kelimeleri yüksek frekans aldıkları için modelin kararını gereksiz yere domine edebilir.*
>
> *`TF-IDF` (Term Frequency - Inverse Document Frequency) ise iki temel gücü birleştirir:*
> 1. *Bir terim bir belgede çok sık geçiyorsa önem kazanır ($TF$).*
> 2. *Ancak o terim veri setindeki tüm belgelerde çok yaygınsa (örneğin 'experience', 'company' gibi), formüldeki $IDF = \log(N / DF)$ bileşeni sayesinde ağırlığı düşürülür.*
>
> *Ayrıca `ngram_range=(1, 2)` kullanarak hem tekil kelimeleri ('learning') hem de teknik ikili kalıpları ('machine learning', 'deep learning', 'rest api') yakaladık."*

---

### Soru 3: Pozisyon sınıflandırmasında 4 farklı modeli (Naive Bayes, KNN, SVM, Random Forest) neden kıyasladınız ve sonuçlar ne oldu?

**Cevap:**
> *"Farklı algoritmalar metin verisinde farklı matematiksel varsayımlarla çalışır:*
> * **Naive Bayes (MultinomialNB):** Kelimelerin birbirinden bağımsız olduğu varsayımıyla koşullu olasılık hesaplar ($P(\text{Rol} \mid \text{Kelimeler})$). Çok az parametreyle çok hızlı eğitilir ve metin sınıflandırmada güçlü bir temel oluşturur.
> * **KNN (K-Nearest Neighbors):** Öklid mesafesi ve çoğunluk oyuyla çalışır. Yüksek boyutlu TF-IDF uzayında boyutun laneti (Curse of Dimensionality) nedeniyle test aşamasında daha yavaştır.
> * **SVM (Support Vector Machine):** Sınıflar arasında marjini maksimize eden optimal hiper-düzlemi bulur. Metin uzayı gibi yüksek boyutlu ve seyrek (sparse) verilerde mükemmel bir ayrım sunar.
> * **Random Forest:** 100 karar ağacının oylamasıyla (Bagging) varyansı düşürür ve aşırı öğrenmeyi (Overfitting) engeller.
>
> *Tüm modellerimizi tek bir train-test ayrımıyla değil, **5-Katlı Çapraz Doğrulama (5-Fold CV)** ile test ederek tarafsız bir şekilde kıyasladık."*

---

### Soru 4: Aşırı Öğrenmeyi (Overfitting) önlemek için projede hangi tedbirleri aldınız?

**Cevap:**
> *"Üç temel mühendislik önlemi uyguladık:*
> 1. *Veriyi tek bir sefer %80-%20 bölüp sonuca güvenmek yerine, Scikit-Learn `cross_val_score` ile **5-Katlı Çapraz Doğrulama (K-Fold CV)** çalıştırdık. Böylece model veri setinin her parçasında test edildi.*
> 2. *`TfidfVectorizer` üzerinde `max_features=2500` sınırı koyarak nadir geçen gürültü kelimelerin modeli ezberletmesini engelledik.*
> 3. *Random Forest modelinde ağaç derinliğini ve `n_estimators=100` parametresini kontrol altında tuttuk."*

---

### Soru 5: Bu projeyi günde 500.000 CV işleyen gerçek bir kurumsal ortama (Production) taşısaydınız mimariyi nasıl dönüştürürdünüz?

**Cevap:**
> *"Böyle bir ölçek için şu iyileştirmeleri yapardım:*
> 1. *Model Çıkarımını (Inference) Hızlandırma: Eğitilmiş TF-IDF ve sınıflandırıcı modellerini **ONNX Runtime** formatına dönüştürüp CPU üzerinde mikrosaniye seviyesinde tahmin alırdım.*
> 2. *Vektör Arama Motoru (Vector Database): Milyonlarca iş ilanı ve CV arasındaki kosinüs benzerliğini hesaplamak için **FAISS**, **Milvus** veya **Qdrant** gibi Approximate Nearest Neighbor (ANN) vektör veri tabanlarını entegre ederdim.*
> 3. *Kuyruk ve Asenkron Mimari: CV ayrıştırma (parsing) ve NLP işlemlerini **Celery + Redis** veya **RabbitMQ** ile arka plan iş kuyruklarına dağıtırdım.*
> 4. *Mikroservis Mimarisi: Streamlit arayüzünü **FastAPI** arkasında konteynerize edip (Docker) **Kubernetes (K8s)** üzerinde yatay olarak ölçeklerdim (Auto-scaling)."*

