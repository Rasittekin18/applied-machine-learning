import pytest
import numpy as np
import pandas as pd
from JobFit_AI.src.model_evaluator import ModelEvaluator

def test_get_benchmark_dataframe():
    sample_bench = {
        "Model A": {"cv_mean": 0.95, "test_accuracy": 0.96},
        "Model B": {"cv_mean": 0.91, "test_accuracy": 0.92}
    }
    df = ModelEvaluator.get_benchmark_dataframe(sample_bench)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert "Model Adı" in df.columns
    assert "Test Seti Doğruluğu (%)" in df.columns
    # Model A should be top (sorted descending)
    assert df.iloc[0]["Model Adı"] == "Model A"

def test_plot_confusion_matrix():
    cm = np.array([
        [20, 1],
        [2, 19]
    ])
    classes = ["Cat", "Dog"]
    fig = ModelEvaluator.plot_confusion_matrix(cm, classes, title="Test CM")
    assert fig is not None
    import matplotlib.pyplot as plt
    plt.close(fig)

def test_plot_benchmark_comparison():
    df = pd.DataFrame({
        "Model Adı": ["NB", "KNN"],
        "Test Seti Doğruluğu (%)": [98.5, 95.0]
    })
    fig = ModelEvaluator.plot_benchmark_comparison(df)
    assert fig is not None
    import matplotlib.pyplot as plt
    plt.close(fig)

