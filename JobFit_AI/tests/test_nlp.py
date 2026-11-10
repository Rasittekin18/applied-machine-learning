import pytest
from JobFit_AI.src.nlp_preprocessor import NLPPreprocessor

@pytest.fixture
def preprocessor():
    return NLPPreprocessor()

def test_clean_text_basic(preprocessor):
    text = "We are seeking a Python developer with 3 years experience."
    cleaned = preprocessor.clean_text(text)
    assert "python" in cleaned
    assert "develop" in cleaned
    # Stopwords & noise should be removed
    assert "seeking" not in cleaned
    assert "years" not in cleaned
    assert "experience" not in cleaned

def test_clean_text_special_terms(preprocessor):
    text = "Skills: C++, C#, .NET, Node.js, React.js"
    cleaned = preprocessor.clean_text(text)
    assert "cpp" in cleaned
    assert "csharp" in cleaned
    assert "dotnet" in cleaned
    assert "nodejs" in cleaned
    assert "react" in cleaned

def test_clean_text_empty_and_edge_cases(preprocessor):
    assert preprocessor.clean_text("") == ""
    assert preprocessor.clean_text(None) == ""
    assert preprocessor.clean_text("   \n\t  ") == ""
    assert preprocessor.clean_text("12345 !@#$%^&*()") == ""
    assert preprocessor.clean_text("https://google.com/careers test@example.com") == ""

def test_tfidf_vectorization(preprocessor):
    corpus = [
        "Python developer building machine learning models with PyTorch.",
        "Frontend engineer working with React, TypeScript, and HTML.",
        "DevOps engineer managing Kubernetes clusters on AWS cloud."
    ]
    matrix = preprocessor.fit_transform(corpus)
    assert matrix.shape[0] == 3
    assert matrix.shape[1] > 0
    
    # Transform unseen text
    test_vec = preprocessor.transform("Python and PyTorch machine learning")
    assert test_vec.shape[0] == 1
    assert test_vec.shape[1] == matrix.shape[1]

def test_extract_keywords(preprocessor):
    text = "Python Python Python Docker Docker AWS"
    kw = preprocessor.extract_keywords(text, top_n=2)
    assert len(kw) == 2
    assert kw[0][0] == "python"
    assert kw[0][1] == 3
    assert kw[1][0] == "docker"
    assert kw[1][1] == 2

