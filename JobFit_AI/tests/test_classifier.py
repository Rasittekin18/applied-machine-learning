import pytest
import os
from JobFit_AI.src.classifier import JobClassifierTrainer

@pytest.fixture(scope="module")
def trainer():
    t = JobClassifierTrainer()
    t.load_artifacts()
    return t

def test_models_loaded(trainer):
    assert trainer.best_role_model is not None
    assert trainer.level_model is not None
    assert trainer.preprocessor.is_fitted is True

def test_predict_role_data_science(trainer):
    text = "Building deep learning neural networks with PyTorch, data analysis with Pandas, and Scikit-Learn pipelines in Python."
    pred = trainer.predict_role_and_level(text)
    assert pred["predicted_role"] == "Data Science & AI"
    assert pred["role_confidence"] > 50.0

def test_predict_role_frontend(trainer):
    text = "Frontend engineer building responsive UI using React, Next.js, TypeScript, and Tailwind CSS."
    pred = trainer.predict_role_and_level(text)
    assert pred["predicted_role"] == "Frontend Development"
    assert pred["role_confidence"] > 50.0

def test_predict_role_devops(trainer):
    text = "Automating CI/CD pipelines with Jenkins and managing Kubernetes clusters on AWS with Terraform."
    pred = trainer.predict_role_and_level(text)
    assert pred["predicted_role"] == "DevOps & Cloud"
    assert pred["role_confidence"] > 50.0

def test_predict_role_backend(trainer):
    text = "Developing scalable REST APIs using FastAPI, Django, PostgreSQL, Redis, and microservices architecture."
    pred = trainer.predict_role_and_level(text)
    assert pred["predicted_role"] == "Backend Development"
    assert pred["role_confidence"] > 50.0

def test_level_prediction(trainer):
    text = "5+ years of extensive leadership leading engineering teams, distributed architectures, and mentoring."
    pred = trainer.predict_role_and_level(text)
    assert pred["predicted_level"] in ["Junior", "Mid", "Senior"]
    assert 0.0 <= pred["level_confidence"] <= 100.0

