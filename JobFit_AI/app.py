import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib

# Sayfa Yapılandırması
st.set_page_config(
    page_title="JobFit AI - Akıllı CV & İş İlanı Analizörü",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modül importları (Güvenli import)
try:
    from JobFit_AI.src.nlp_preprocessor import NLPPreprocessor
    from JobFit_AI.src.recommender import JobFitRecommender
    from JobFit_AI.src.classifier import JobClassifierTrainer
    from JobFit_AI.src.cv_parser import CVParser
    from JobFit_AI.src.model_evaluator import ModelEvaluator
except (ImportError, ValueError):
    from src.nlp_preprocessor import NLPPreprocessor
    from src.recommender import JobFitRecommender
    from src.classifier import JobClassifierTrainer
    from src.cv_parser import CVParser
    from src.model_evaluator import ModelEvaluator

# Özel CSS Tasarımı
st.markdown("""
<style>
    .main-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #1e3d59;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 1.5rem;
    }
    .score-card {
        background: linear-gradient(135deg, #1e3d59 0%, #17b978 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .score-number {
        font-size: 3rem;
        font-weight: 800;
        margin: 0;
    }
    .badge-matched {
        display: inline-block;
        background-color: #d4edda;
        color: #155724;
        padding: 4px 10px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
        margin: 3px;
        border: 1px solid #c3e6cb;
    }
    .badge-missing {
        display: inline-block;
        background-color: #f8d7da;
        color: #721c24;
        padding: 4px 10px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
        margin: 3px;
        border: 1px solid #f5c6cb;
    }
    .badge-extra {
        display: inline-block;
        background-color: #e2e3e5;
        color: #383d41;
        padding: 4px 10px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
        margin: 3px;
    }
</style>
""", unsafe_allow_html=True)

# Cache ile Modelleri Yükleme
@st.cache_resource
def load_components():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(base_dir, "models")
    
    recommender = JobFitRecommender()
    classifier = JobClassifierTrainer()
    
    # Model dosyaları mevcut mu?
    role_path = os.path.join(models_dir, "role_classifier.joblib")
    if os.path.exists(role_path):
        classifier.load_artifacts(models_dir)
    else:
        # Eğitilmemişse eğit
        classifier.train_and_benchmark_roles()
        classifier.save_artifacts(models_dir)
        
    return recommender, classifier

recommender, classifier = load_components()

# Örnek Şablon Veriler
SAMPLE_CV = """John Doe
Senior Data Scientist & Machine Learning Engineer
Email: john.doe@email.com | GitHub: github.com/johndoe

Summary:
Data Scientist with 5+ years of experience designing and deploying machine learning pipelines,
statistical modeling, and feature engineering at scale.

Technical Skills:
- Languages & Core: Python, SQL, R, Bash, Git
- ML & Deep Learning: Scikit-Learn, Pandas, NumPy, Machine Learning, Data Analysis, Statistics
- Database & Tools: PostgreSQL, MySQL, Docker, Jupyter

Work Experience:
- Led end-to-end churn prediction model development using Scikit-Learn, improving retention by 18%.
- Conducted exploratory data analysis and feature engineering on 10M+ customer interaction records.
"""

SAMPLE_JOB = """We are actively seeking an experienced Machine Learning Engineer / Data Scientist to join our AI team.

Key Responsibilities:
- Design, train, and optimize predictive machine learning and deep learning models.
- Build production-ready NLP and computer vision pipelines.
- Containerize services using Docker and deploy scalable microservices on AWS or Kubernetes.
- Collaborate with engineering teams to integrate REST APIs built with FastAPI.

Required Qualifications:
- 5+ years of software engineering / data science experience.
- Proficiency in Python, SQL, Pandas, Scikit-Learn, and Machine Learning.
- Hands-on experience with PyTorch or TensorFlow for Deep Learning architectures.
- Experience with Docker, Kubernetes, FastAPI, and Git version control.
- Strong analytical thinking and problem solving skills.
"""

# Yan Panel (Sidebar)
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/resume.png", width=120)
    st.title("💼 JobFit AI")
    st.markdown("**Akıllı CV & İş İlanı Eşleştirici**")
    st.caption("A'dan Z'ye Makine Öğrenmesi Kursu Bitirme Projesi")
    st.divider()

    st.markdown("### ⚙️ Hızlı Şablon")
    if st.button("📋 Örnek CV ve İlanı Yükle", use_container_width=True):
        st.session_state["cv_input"] = SAMPLE_CV
        st.session_state["job_input"] = SAMPLE_JOB

    st.divider()
    st.markdown("### 🧠 Kullanılan ML Teknikleri")
    st.markdown("""
    - **NLP (Bölüm 18):** Regex, Tokenization, Stemming, TF-IDF
    - **Öneri Sistemleri (Bölüm 21):** Kosinüs Benzerliği (Cosine Similarity) & Skill Gap
    - **Sınıflandırma (Bölüm 10, 11, 14):** Naive Bayes, KNN, SVM, Random Forest
    - **Model Seçimi (Bölüm 20):** 5-Fold Cross Validation
    - **Metrikler (Bölüm 15):** Confusion Matrix & F1-Score
    """)

# Ana Başlık
st.markdown('<div class="main-title">💼 JobFit AI: CV & İş İlanı Uygunluk Analizörü</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Yapay zeka ile CV\'nizi iş ilanlarıyla karşılaştırın, eksik yeteneklerinizi (Skill Gap) keşfedin ve ATS puanınızı artırın.</div>', unsafe_allow_html=True)

# Sekmeler
tab_match, tab_classify, tab_models = st.tabs([
    "🎯 CV & İlan Eşleştirme (Recommender)",
    "🤖 Pozisyon & Kıdem Sınıflandırıcı",
    "📊 Model Laboratuvarı & Kıyaslama"
])

# ==========================================
# SEKME 1: CV & İLAN EŞLEŞTİRME
# ==========================================
with tab_match:
    col_cv, col_job = st.columns(2)

    with col_cv:
        st.subheader("📄 1. Özgeçmişiniz (CV)")
        cv_file = st.file_uploader("CV Dosyası Yükleyin (PDF, DOCX, TXT):", type=["pdf", "docx", "txt"])
        
        default_cv = st.session_state.get("cv_input", "")
        if cv_file is not None:
            parsed_cv = CVParser.parse(cv_file, cv_file.name)
            cv_text = st.text_area("Veya CV Metnini Düzenleyin:", value=parsed_cv, height=280)
        else:
            cv_text = st.text_area("Veya CV Metnini Buraya Yapıştırın:", value=default_cv, height=280)

    with col_job:
        st.subheader("📌 2. Hedef İş İlanı")
        default_job = st.session_state.get("job_input", "")
        job_text = st.text_area(
            "İş İlanı Metnini / Gereksinimlerini Buraya Yapıştırın:",
            value=default_job,
            height=345,
            placeholder="Pozisyon açıklaması, aranan nitelikler ve teknolojiler..."
        )

    btn_analyze = st.button("🚀 Uyum Analizini Başlat", type="primary", use_container_width=True)

    if btn_analyze:
        if not cv_text.strip() or not job_text.strip():
            st.warning("⚠️ Lütfen analiz yapabilmek için hem CV metnini hem de İş İlanını giriniz.")
        else:
            with st.spinner("NLP pipeline çalıştırılıyor, yetkinlikler taranıyor ve uyum hesaplanıyor..."):
                # Öneri ve eşleştirme analizi
                report = recommender.analyze_fit(cv_text, job_text, vectorizer=classifier.preprocessor.vectorizer)
                # ML ile rol ve kıdem tahmini
                cv_pred = classifier.predict_role_and_level(cv_text)
                job_pred = classifier.predict_role_and_level(job_text)

            st.divider()

            # Skor Kartları
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.metric(
                    label="🎯 Genel Uyum Skoru",
                    value=f"%{report['overall_score']}",
                    delta=f"{report['overall_score'] - 50:.1f}% Eşik Farkı"
                )
            with c2:
                st.metric(label="🧠 Semantik Benzerlik", value=f"%{report['semantic_score']}")
            with c3:
                st.metric(label="⚡ Beceri Örtüşmesi", value=f"%{report['skill_score']}")
            with c4:
                st.metric(
                    label="🔍 Eşleşen Beceri",
                    value=f"{len(report['matched_skills'])} / {report['total_job_skills_count']}"
                )

            # İlerleme Çubuğu
            st.progress(int(report['overall_score']))

            st.markdown("---")

            # Pozisyon & Kıdem Eşleşmesi
            st.subheader("👔 Yapay Zeka Rol ve Kıdem Tespiti")
            p_col1, p_col2 = st.columns(2)
            with p_col1:
                st.info(f"**CV'nizden Algılanan Profil:** {cv_pred['predicted_role']} ({cv_pred['predicted_level']}) — Güven: %{cv_pred['role_confidence']}")
            with p_col2:
                st.success(f"**İlandan Algılanan Profil:** {job_pred['predicted_role']} ({job_pred['predicted_level']}) — Güven: %{job_pred['role_confidence']}")

            # Beceri Analizi ve Skill Gap
            st.subheader("🧩 Beceri Analizi (Skill Gap)")
            b_col1, b_col2, b_col3 = st.columns(3)

            with b_col1:
                st.markdown("#### ✅ Eşleşen Beceriler")
                if report["matched_skills"]:
                    badges = "".join([f'<span class="badge-matched">{s}</span>' for s in report["matched_skills"]])
                    st.markdown(badges, unsafe_allow_html=True)
                else:
                    st.caption("Ortak yetkinlik bulunamadı.")

            with b_col2:
                st.markdown("#### ❌ Eksik Beceriler (Skill Gap)")
                if report["missing_skills"]:
                    badges = "".join([f'<span class="badge-missing">{s}</span>' for s in report["missing_skills"]])
                    st.markdown(badges, unsafe_allow_html=True)
                else:
                    st.caption("Eksik beceri yok, harika!")

            with b_col3:
                st.markdown("#### 💡 CV'nizdeki Ekstra Beceriler")
                if report["extra_skills"]:
                    badges = "".join([f'<span class="badge-extra">{s}</span>' for s in report["extra_skills"][:10]])
                    st.markdown(badges, unsafe_allow_html=True)
                else:
                    st.caption("Ekstra beceri bulunamadı.")

            st.markdown("---")

            # Radar / Spider Chart ile Kategori Bazlı Uyum
            import plotly.graph_objects as go
            st.subheader("🕸️ Kategori Bazlı Yetkinlik Haritası (Radar Analizi)")
            
            categories_radar = list(report["category_breakdown"].keys())
            job_req_counts = [report["category_breakdown"][c]["job_count"] for c in categories_radar]
            cv_match_counts = [report["category_breakdown"][c]["cv_count"] for c in categories_radar]
            
            # Kapatmak için ilk elemanı sona ekle
            categories_radar_closed = categories_radar + [categories_radar[0]]
            job_req_closed = job_req_counts + [job_req_counts[0]]
            cv_match_closed = cv_match_counts + [cv_match_counts[0]]

            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatterpolar(
                r=job_req_closed,
                theta=categories_radar_closed,
                fill='toself',
                name='İlanda Aranan Yetkinlik Sayısı',
                line_color='#e74c3c'
            ))
            fig_radar.add_trace(go.Scatterpolar(
                r=cv_match_closed,
                theta=categories_radar_closed,
                fill='toself',
                name='CV\'nizdeki Yetkinlik Sayısı',
                line_color='#2ecc71'
            ))
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True, range=[0, max(max(job_req_counts + cv_match_counts, default=5) + 1, 5)])
                ),
                showlegend=True,
                margin=dict(l=40, r=40, t=30, b=30),
                height=400
            )
            st.plotly_chart(fig_radar, use_container_width=True)

            st.markdown("---")

            # Eylem Planı ve Tavsiyeler
            st.subheader("📋 Kişiselleştirilmiş ATS ve Kariyer Eylem Planı")
            for r in report["recommendations"]:
                st.markdown(r)

            # Rapor İndirme Butonu
            report_markdown = f"""# JobFit AI - CV & İş İlanı Uygunluk Analiz Raporu
Tarih: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}

## 1. Skor Özeti
- **Genel Uyum Skoru:** %{report['overall_score']}
- **Semantik Benzerlik:** %{report['semantic_score']}
- **Doğrudan Beceri Örtüşmesi:** %{report['skill_score']}
- **Eşleşen Beceri Oranı:** {len(report['matched_skills'])} / {report['total_job_skills_count']}

## 2. Profil Tespiti
- **CV Profil Tahmini:** {cv_pred['predicted_role']} ({cv_pred['predicted_level']})
- **İlan Profil Tahmini:** {job_pred['predicted_role']} ({job_pred['predicted_level']})

## 3. Yetkinlik Analizi
- **Eşleşen Beceriler:** {', '.join(report['matched_skills']) if report['matched_skills'] else 'Yok'}
- **Eksik Beceriler (Skill Gap):** {', '.join(report['missing_skills']) if report['missing_skills'] else 'Yok'}
- **Ekstra Yetkinlikler:** {', '.join(report['extra_skills']) if report['extra_skills'] else 'Yok'}

## 4. Eylem Planı ve Tavsiyeler
{chr(10).join(['- ' + rec.replace('*', '') for rec in report['recommendations']])}
"""
            st.download_button(
                label="📥 Detaylı ATS Raporunu İndir (.md)",
                data=report_markdown,
                file_name="JobFit_AI_Analiz_Raporu.md",
                mime="text/markdown",
                use_container_width=True
            )

# ==========================================
# SEKME 2: POZİSYON VE KIDEM SINIFLANDIRICI
# ==========================================
with tab_classify:
    st.subheader("🤖 Pozisyon ve Kıdem Seviyesi Tahmin Edici")
    st.markdown("Herhangi bir iş ilanı veya serbest metin girin; eğittiğimiz makine öğrenmesi modeli rolü ve kıdem seviyesini anında sınıflandırsın.")
    
    classify_input = st.text_area(
        "Analiz Edilecek Metin:",
        height=180,
        placeholder="Örnek: Looking for a Senior DevOps Engineer with Docker, Kubernetes, AWS, Terraform, CI/CD experience..."
    )
    
    if st.button("🔍 Sınıflandır", key="btn_classify"):
        if classify_input.strip():
            with st.spinner("Model tahmin üretiyor..."):
                pred = classifier.predict_role_and_level(classify_input)
                skills_found = recommender.extract_skills(classify_input)
                
            c_res1, c_res2 = st.columns(2)
            with c_res1:
                st.success(f"### 🏷️ Tahmin Edilen Pozisyon: **{pred['predicted_role']}**")
                st.caption(f"Model Olasılık / Güven Oranı: %{pred['role_confidence']}")
            with c_res2:
                st.info(f"### 🎖️ Tahmin Edilen Kıdem: **{pred['predicted_level']}**")
                st.caption(f"Model Olasılık / Güven Oranı: %{pred['level_confidence']}")
                
            if skills_found:
                st.markdown("**Metinde Tespit Edilen Beceriler:**")
                badges = "".join([f'<span class="badge-matched">{s}</span>' for s in skills_found])
                st.markdown(badges, unsafe_allow_html=True)
        else:
            st.warning("Lütfen metin giriniz.")

# ==========================================
# SEKME 3: MODEL LABORATUVARI & KIYASLAMA
# ==========================================
with tab_models:
    st.subheader("📊 Makine Öğrenmesi Algoritmaları Kıyaslama Laboratuvarı")
    st.markdown("""
    Kurs boyunca öğrendiğimiz 4 temel sınıflandırma algoritması aynı veri kümesi üzerinde 
    **5-Katlı Çapraz Doğrulama (5-Fold Cross Validation)** ve **Test Doğruluğu** ile yarıştırılmıştır.
    """)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    summary_path = os.path.join(base_dir, "models", "benchmark_summary.joblib")
    
    if os.path.exists(summary_path):
        benchmark_dict = joblib.load(summary_path)
        df_bench = ModelEvaluator.get_benchmark_dataframe(benchmark_dict)
        
        col_t, col_g = st.columns([1, 1])
        with col_t:
            st.markdown("#### 🏆 Algoritma Başarı Tablosu")
            st.dataframe(df_bench, use_container_width=True, hide_index=True)
            
            st.markdown("""
            > **Not:** 
            > - **Naive Bayes:** Kelime frekanslarına dayalı metin sınıflandırmasında teorik olarak çok güçlüdür.
            > - **SVM:** Marjini maksimize ederek yüksek boyutlu TF-IDF uzayında mükemmel bir ayrım sunar.
            > - **Random Forest:** Aşırı öğrenmeyi (Overfitting) engelleyerek genellenebilirlik sağlar.
            """)

        with col_g:
            st.markdown("#### 📈 Model Başarı Grafiği")
            fig = ModelEvaluator.plot_benchmark_comparison(df_bench)
            st.pyplot(fig)

        st.markdown("---")
        st.subheader("🔬 Karmaşıklık Matrisi (Confusion Matrix - Bölüm 15)")
        selected_model_name = st.selectbox("İncelemek İstediğiniz Modeli Seçin:", list(benchmark_dict.keys()))
        
        cm_data = np.array(benchmark_dict[selected_model_name]["confusion_matrix"])
        roles = sorted(["Data Science & AI", "Backend Development", "Frontend Development", "DevOps & Cloud"])
        
        fig_cm = ModelEvaluator.plot_confusion_matrix(
            cm_data, roles, title=f"{selected_model_name} - Karmaşıklık Matrisi"
        )
        st.pyplot(fig_cm)
    else:
        st.info("Kıyaslama verileri bulunamadı. Lütfen önce `classifier.py` dosyasını çalıştırın.")

st.markdown("---")
st.caption("JobFit AI © 2026 | Machine Learning & NLP ile Geliştirilmiştir | GitHub İçin Hazır Proje")

