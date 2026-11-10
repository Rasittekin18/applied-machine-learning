import re
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Temel İngilizce ve Mesleki Dolgu Kelimeleri (Self-contained, harici internet indirmesi gerektirmez)
ENGLISH_STOPWORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and",
    "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being",
    "below", "between", "both", "but", "by", "can", "can't", "cannot", "could",
    "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down",
    "during", "each", "few", "for", "from", "further", "had", "hadn't", "has",
    "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her",
    "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's",
    "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it",
    "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
    "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't",
    "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such",
    "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then",
    "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've",
    "this", "those", "through", "to", "too", "under", "until", "up", "very", "was",
    "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what",
    "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's",
    "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd",
    "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves",
    # Mesleki gürültü dolgu kelimeleri
    "experience", "years", "work", "working", "team", "role", "candidate", "strong",
    "knowledge", "skills", "ability", "responsibilities", "qualifications", "required",
    "requirements", "plus", "understanding", "must", "familiarity", "seeking", "join",
    "growing", "talented", "motivated", "looking", "responsible", "actively", "demonstrated"
}

# Kök bulma (Stemming) sırasında bozulmaması gereken teknik kelimeler
STEM_PROTECTED = {
    "nodejs", "pandas", "redis", "kubernetes", "postgres", "express", "devops",
    "aws", "css", "csharp", "dotnet", "ansible", "jenkins", "rails", "cypress",
    "jest", "linux", "sass", "less", "keras", "transformers"
}

def simple_stem(word):
    """
    Hafif ve hızlı kelime kökü (Stemming) kural motoru.
    Teknik korumalı kelimelere dokunmaz, diğerlerinde ekleri temizler.
    """
    if len(word) <= 3 or word in STEM_PROTECTED:
        return word
    # Çift 's' ile biten kelimeleri (express, access vb.) bozma
    if word.endswith("ss"):
        return word
    for suffix in ["tion", "ing", "ly", "ed", "es", "s"]:
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            stemmed = word[:-len(suffix)]
            if stemmed not in STEM_PROTECTED:
                return stemmed
    return word

class NLPPreprocessor:
    """
    Kursun 18. Bölümünde (NLP) öğretilen metin ön işleme adımlarını uygular:
    1. Regex Temizliği (URL, e-posta, telefon, özel karakterler)
    2. Teknik terim normalizasyonu (C++ -> cpp, C# -> csharp)
    3. Lowercasing (Küçük harfe çevirme)
    4. Tokenization (Kelimelere ayırma)
    5. Stopwords Temizliği
    6. Kök Bulma (Stemming / Lemmatization)
    7. TF-IDF Vektörleştirme (TfidfVectorizer)
    """
    def __init__(self, max_features=3000):
        self.max_features = max_features
        self.stop_words = ENGLISH_STOPWORDS
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            ngram_range=(1, 2),
            sublinear_tf=True
        )
        self.is_fitted = False

    def clean_text(self, text):
        """
        Ham metni temizleyip tokenize ve stem edilmiş tek bir metne dönüştürür.
        """
        if not isinstance(text, str):
            return ""

        # 1. URL'leri ve web linklerini kaldır
        text = re.sub(r"https?://\S+|www\.\S+", " ", text)
        
        # 2. E-posta adreslerini kaldır
        text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", " ", text)

        # 3. Kritik teknik terimleri koru ve normalize et
        text = text.replace("c++", "cpp").replace("C++", "cpp")
        text = text.replace("c#", "csharp").replace("C#", "csharp")
        text = text.replace(".net", "dotnet").replace(".NET", "dotnet")
        text = text.replace("node.js", "nodejs").replace("Node.js", "nodejs")
        text = text.replace("vue.js", "vue").replace("Vue.js", "vue")
        text = text.replace("react.js", "react").replace("React.js", "react")

        # 4. Sadece harfleri tut (Regex: [^a-zA-Z\s])
        text = re.sub(r"[^a-zA-Z\s]", " ", text)

        # 5. Küçük harfe dönüştür
        text = text.lower()

        # 6. Tokenization (Kelimelere ayırma)
        tokens = text.split()

        # 7. Stopwords filtreleme ve Kök bulma (Stemming)
        cleaned_tokens = [
            simple_stem(token)
            for token in tokens
            if token not in self.stop_words and len(token) > 1
        ]

        return " ".join(cleaned_tokens)

    def fit_transform(self, corpus):
        """
        Veri kümesindeki metinleri temizler ve TF-IDF matrisini öğrenip dönüştürür.
        """
        cleaned_corpus = [self.clean_text(doc) for doc in corpus]
        tfidf_matrix = self.vectorizer.fit_transform(cleaned_corpus)
        self.is_fitted = True
        return tfidf_matrix

    def transform(self, texts):
        """
        Yeni gelen metinleri (örneğin adayın CV'si veya iş ilanı) TF-IDF vektörüne dönüştürür.
        """
        if not self.is_fitted:
            raise ValueError("Vectorizer henüz eğitilmedi (fit edilmedi)!")
        if isinstance(texts, str):
            texts = [texts]
        cleaned_texts = [self.clean_text(doc) for doc in texts]
        return self.vectorizer.transform(cleaned_texts)

    def extract_keywords(self, text, top_n=10):
        """
        Metin içindeki en sık geçen teknik anahtar kelimeleri ve frekanslarını çeker.
        """
        cleaned = self.clean_text(text)
        words = cleaned.split()
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        sorted_kw = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return sorted_kw[:top_n]

    def save(self, path="JobFit_AI/models/tfidf_vectorizer.joblib"):
        import os
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump(self.vectorizer, path)

    def load(self, path="JobFit_AI/models/tfidf_vectorizer.joblib"):
        self.vectorizer = joblib.load(path)
        self.is_fitted = True

if __name__ == "__main__":
    preprocessor = NLPPreprocessor()
    sample_text = (
        "We are actively seeking a Senior Machine Learning Engineer with 5+ years of experience. "
        "Candidate must have strong expertise in Python, PyTorch, Docker, and NLP pipelines! "
        "Visit https://example.com/careers or email contact@jobfit.ai."
    )
    cleaned = preprocessor.clean_text(sample_text)
    print("Orijinal Metin:\n", sample_text)
    print("\nTemizlenmiş Metin (NLP Pipeline):\n", cleaned)
    print("\nEn Önemli Kelimeler:\n", preprocessor.extract_keywords(sample_text))
