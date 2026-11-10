import pytest
import plotly.graph_objects as go
from JobFit_AI.src.recommender import JobFitRecommender
from JobFit_AI.src.classifier import JobClassifierTrainer

def test_app_end_to_end_flow():
    recommender = JobFitRecommender()
    classifier = JobClassifierTrainer()
    classifier.load_artifacts()

    cv_text = "Senior Data Scientist with Python, SQL, Machine Learning, PyTorch, Docker, and Pandas."
    job_text = "Looking for Machine Learning Engineer with Python, Scikit-Learn, PyTorch, Docker, and AWS."

    report = recommender.analyze_fit(cv_text, job_text, vectorizer=classifier.preprocessor.vectorizer)
    assert report["overall_score"] > 0.0

    cv_pred = classifier.predict_role_and_level(cv_text)
    job_pred = classifier.predict_role_and_level(job_text)

    assert cv_pred["predicted_role"] == "Data Science & AI"
    assert job_pred["predicted_role"] == "Data Science & AI"

    # Radar Chart verification
    breakdown = report["category_breakdown"]
    cats = list(breakdown.keys())
    job_counts = [breakdown[c]["job_count"] for c in cats]
    cv_counts = [breakdown[c]["cv_count"] for c in cats]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=job_counts + [job_counts[0]], theta=cats + [cats[0]]))
    fig.add_trace(go.Scatterpolar(r=cv_counts + [cv_counts[0]], theta=cats + [cats[0]]))
    assert fig is not None

