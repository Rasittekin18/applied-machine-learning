import pytest
from JobFit_AI.src.recommender import JobFitRecommender

@pytest.fixture
def recommender():
    return JobFitRecommender()

def test_extract_skills(recommender):
    text = "Proficient in Python, Machine Learning, Docker, and React. Experience with SQL and AWS."
    skills = recommender.extract_skills(text)
    assert "python" in skills
    assert "machine learning" in skills
    assert "docker" in skills
    assert "react" in skills
    assert "sql" in skills
    assert "aws" in skills

def test_extract_skills_word_boundary(recommender):
    # Should NOT falsely match 'r' inside 'regular' or 'go' inside 'good'
    text = "A regular employee doing good work."
    skills = recommender.extract_skills(text)
    assert "r" not in skills
    assert "go" not in skills

def test_analyze_fit_high_match(recommender):
    cv = "Machine learning engineer skilled in Python, Scikit-Learn, Pandas, NumPy, SQL, and Git."
    job = "Hiring ML engineer with Python, Scikit-Learn, Pandas, SQL, and Git."
    
    report = recommender.analyze_fit(cv, job)
    assert report["overall_score"] > 60.0
    assert len(report["matched_skills"]) >= 4
    assert len(report["recommendations"]) > 0
    assert "category_breakdown" in report

def test_analyze_fit_zero_match(recommender):
    cv = "Cook with deep passion for culinary arts, pastry, and kitchen operations."
    job = "DevOps Engineer required with Terraform, Kubernetes, Docker, AWS, and Linux."
    
    report = recommender.analyze_fit(cv, job)
    assert report["overall_score"] < 15.0
    assert len(report["matched_skills"]) == 0
    assert len(report["missing_skills"]) > 0

def test_analyze_fit_empty_input(recommender):
    report = recommender.analyze_fit("", "")
    assert isinstance(report["overall_score"], (int, float))
    assert report["matched_skills"] == []
    assert report["missing_skills"] == []

def test_category_breakdown_keys(recommender):
    cv = "Python, Pandas, Docker, React"
    job = "Python, PyTorch, Kubernetes"
    report = recommender.analyze_fit(cv, job)
    breakdown = report["category_breakdown"]
    
    expected_categories = ["Data Science & AI", "Backend Development", "Frontend Development", "DevOps & Cloud"]
    for cat in expected_categories:
        assert cat in breakdown
        assert "job_count" in breakdown[cat]
        assert "cv_count" in breakdown[cat]
        assert "match_pct" in breakdown[cat]

