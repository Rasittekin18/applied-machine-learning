import json
import os
import re
from sklearn.metrics.pairwise import cosine_similarity
try:
    from .nlp_preprocessor import NLPPreprocessor
except (ImportError, ValueError):
    from JobFit_AI.src.nlp_preprocessor import NLPPreprocessor

class JobFitRecommender:
    """
    Kursun 21. Bölümünde (Öneri Sistemleri) işlenen
    Kosinüs Benzerliği (Cosine Similarity) ve İçerik Tabanlı Filtreleme (Content-Based Filtering)
    yaklaşımını uygulayan öneri motoru.
    """
    def __init__(self, skills_dict_path=None):
        if skills_dict_path is None:
            # Otomatik path tespiti
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            skills_dict_path = os.path.join(base_dir, "data", "skills_dictionary.json")
            
        with open(skills_dict_path, "r", encoding="utf-8") as f:
            self.skills_taxonomy = json.load(f)
            
        # Tüm becerileri tek bir liste haline getir
        self.all_skills = []
        for cat, skills in self.skills_taxonomy.items():
            self.all_skills.extend(skills)
        # Uzun ifadelerin önce eşleşmesi için uzunluğa göre azalan sırala
        self.all_skills = sorted(list(set(self.all_skills)), key=lambda s: len(s), reverse=True)
        
        self.preprocessor = NLPPreprocessor()

    def extract_skills(self, text):
        """
        Verilen metin içindeki teknik becerileri Regex yardımıyla yakalar.
        """
        if not isinstance(text, str):
            return []
        
        text_lower = " " + text.lower() + " "
        # Noktalama işaretlerini boşluk yap (ancak +, # gibi özel karakterleri koru)
        cleaned = re.sub(r"[^\w\s+#.]", " ", text_lower)
        
        found_skills = set()
        for skill in self.all_skills:
            # Kelime sınırları ile tam eşleşme ara
            pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
            if re.search(pattern, cleaned):
                found_skills.add(skill)
                
        return sorted(list(found_skills))

    def calculate_semantic_similarity(self, cv_text, job_text, vectorizer=None):
        """
        CV ve İş İlanı metinlerinin TF-IDF vektörleri arasındaki Kosinüs Benzerliğini hesaplar.
        Boş veya anlamsız metinlerde 0.0 döndürerek çökmeleri önler.
        """
        cleaned_cv = self.preprocessor.clean_text(cv_text)
        cleaned_job = self.preprocessor.clean_text(job_text)

        if not cleaned_cv.strip() or not cleaned_job.strip():
            return 0.0

        try:
            if vectorizer is None:
                from sklearn.feature_extraction.text import TfidfVectorizer
                vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)
                tfidf = vec.fit_transform([cleaned_cv, cleaned_job])
                sim = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
            else:
                vec_cv = vectorizer.transform([cleaned_cv])
                vec_job = vectorizer.transform([cleaned_job])
                # Eğer vektörlerin normu sıfırsa
                if vec_cv.nnz == 0 or vec_job.nnz == 0:
                    return 0.0
                sim = cosine_similarity(vec_cv, vec_job)[0][0]
            return float(sim)
        except Exception:
            return 0.0

    def analyze_fit(self, cv_text, job_text, vectorizer=None):
        """
        CV ve İş İlanı arasındaki tam uyum raporunu oluşturur:
        - Semantik Kosinüs Skoru
        - Beceri Eşleşme Skoru
        - Hibrit Toplam Skor
        - Eşleşen, Eksik ve Ekstra Beceriler
        - Somut İyileştirme Tavsiyeleri
        """
        cv_skills = set(self.extract_skills(cv_text))
        job_skills = set(self.extract_skills(job_text))

        matched_skills = sorted(list(cv_skills.intersection(job_skills)))
        missing_skills = sorted(list(job_skills.difference(cv_skills)))
        extra_skills = sorted(list(cv_skills.difference(job_skills)))

        # Beceri oranı
        if len(job_skills) > 0:
            skill_score = (len(matched_skills) / len(job_skills)) * 100
        else:
            skill_score = 100.0

        # Semantik metin benzerliği (0 - 100)
        semantic_sim = self.calculate_semantic_similarity(cv_text, job_text, vectorizer) * 100

        # Hibrit Uyum Skoru (Ağırlıklı ortalama: %50 semantik, %50 doğrudan beceri örtüşmesi)
        hybrid_score = round(0.50 * semantic_sim + 0.50 * skill_score, 1)
        hybrid_score = min(max(hybrid_score, 0.0), 100.0)

        # Akıllı İyileştirme Tavsiyeleri Üretme
        recommendations = self._generate_recommendations(
            hybrid_score, matched_skills, missing_skills
        )

        # Kategori bazlı beceri dağılımı (Radar Chart için)
        category_breakdown = self._calculate_category_breakdown(cv_skills, job_skills)

        return {
            "overall_score": hybrid_score,
            "semantic_score": round(semantic_sim, 1),
            "skill_score": round(skill_score, 1),
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "extra_skills": extra_skills,
            "total_job_skills_count": len(job_skills),
            "recommendations": recommendations,
            "category_breakdown": category_breakdown
        }

    def _calculate_category_breakdown(self, cv_skills, job_skills):
        """
        Radar grafiği için her ana kategorideki beceri eşleşme oranlarını hesaplar.
        """
        breakdown = {}
        for category, cat_skills in self.skills_taxonomy.items():
            if category == "General & Soft Skills":
                continue
            cat_set = set(cat_skills)
            job_cat = job_skills.intersection(cat_set)
            cv_cat = cv_skills.intersection(cat_set)
            
            job_count = len(job_cat)
            cv_count = len(cv_cat)
            
            # Eşleşme yüzdesi
            if job_count > 0:
                match_pct = round((len(cv_cat.intersection(job_cat)) / job_count) * 100, 1)
            else:
                match_pct = 100.0 if cv_count > 0 else 0.0
                
            breakdown[category] = {
                "job_count": job_count,
                "cv_count": cv_count,
                "match_pct": match_pct
            }
        return breakdown

    def _generate_recommendations(self, score, matched, missing):
        recs = []
        
        if score >= 80:
            recs.append("🌟 **Mükemmel Uyum:** CV'niz bu pozisyonun gereksinimleriyle çok yüksek oranda örtüşüyor.")
        elif score >= 60:
            recs.append("👍 **İyi Uyum:** Temel nitelikleri karşılıyorsunuz; birkaç eksik beceriyi vurgulayarak şansınızı artırabilirsiniz.")
        else:
            recs.append("⚠️ **Geliştirilmesi Gereken Uyum:** İlandaki kritik gereksinimlerin önemli bir kısmı CV'nizde yer almıyor.")

        if missing:
            top_missing = missing[:5]
            recs.append(
                f"🎯 **ATS ve Anahtar Kelime Optimizasyonu:** İlanda açıkça aranan şu yetkinlikleri CV'nize eklemeniz tavsiye edilir: **{', '.join(top_missing)}**."
            )
            recs.append(
                "💡 **Proje Vurgusu:** Bu eksik teknolojilerle ilgili geçmişte yaptığınız yan projeleri, GitHub linklerini veya sertifikaları 'Projeler' bölümünde öne çıkarın."
            )
        else:
            recs.append("✅ **Tüm Beceriler Karşılandı:** İlanda belirtilen tüm teknik anahtar kelimeler profilinizde mevcut!")

        return recs

if __name__ == "__main__":
    recommender = JobFitRecommender()
    
    sample_cv = """
    Software Engineer with strong background in Python, Pandas, NumPy, Scikit-Learn, SQL, and Machine Learning.
    Experienced in building predictive models, Git version control, and data analysis.
    """
    
    sample_job = """
    We are looking for a Machine Learning Engineer.
    Requirements:
    - Proficiency in Python, Scikit-Learn, SQL, and Pandas.
    - Hands-on experience with PyTorch or TensorFlow for Deep Learning.
    - Familiarity with Docker and building REST APIs with FastAPI.
    - Strong problem solving and Git skills.
    """
    
    report = recommender.analyze_fit(sample_cv, sample_job)
    print("--- JOBFIT AI ÖNERİ VE EŞLEŞTİRME RAPORU ---")
    print(f"Toplam Uyum Skoru: %{report['overall_score']}")
    print(f"Semantik Benzerlik: %{report['semantic_score']}")
    print(f"Doğrudan Beceri Skoru: %{report['skill_score']}")
    print("Eşleşen Beceriler:", report["matched_skills"])
    print("Eksik Beceriler (Skill Gap):", report["missing_skills"])
    print("\nTavsiyeler:")
    for r in report["recommendations"]:
        print("-", r)

