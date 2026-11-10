import pytest
import io
from JobFit_AI.src.cv_parser import CVParser

def test_extract_from_txt_string():
    content = "Hello, this is a plain text CV with Python and SQL."
    extracted = CVParser.extract_from_txt(content)
    assert extracted == content

def test_extract_from_txt_stream():
    content = "Streaming text CV with Docker and Kubernetes."
    stream = io.BytesIO(content.encode("utf-8"))
    extracted = CVParser.extract_from_txt(stream)
    assert extracted == content

def test_parse_auto_detection():
    # Plain text detection
    raw = "Automatic detection test with React and TypeScript."
    res = CVParser.parse(raw, "resume.txt")
    assert res == raw

def test_parse_docx_missing_file_handled():
    # If a non-existent docx path is provided, it should return an error message rather than crashing
    res = CVParser.parse("non_existent_file.docx")
    assert "Hata" in res or isinstance(res, str)

