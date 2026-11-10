import io
import os

class CVParser:
    """
    Kullanıcının yüklediği PDF, DOCX veya TXT formatındaki CV dosyalarını
    temiz metne dönüştüren yardımcı sınıf.
    """
    @staticmethod
    def extract_from_pdf(file_input):
        """
        PyMuPDF (fitz) kullanarak PDF dosyalarından metin çeker.
        file_input: Dosya yolu (str) veya dosya baytları / stream (io.BytesIO).
        """
        try:
            import fitz  # PyMuPDF
            if isinstance(file_input, str):
                doc = fitz.open(file_input)
            else:
                file_bytes = file_input if isinstance(file_input, (bytes, bytearray)) else file_input.read()
                doc = fitz.open(stream=file_bytes, filetype="pdf")
                
            text_pages = []
            for page in doc:
                text_pages.append(page.get_text())
            doc.close()
            return "\n".join(text_pages).strip()
        except Exception as e:
            return f"PDF Okuma Hatası: {str(e)}"

    @staticmethod
    def extract_from_docx(file_input):
        """
        python-docx kullanarak Word (.docx) belgelerinden metin çeker.
        """
        try:
            import docx
            if isinstance(file_input, str):
                doc = docx.Document(file_input)
            else:
                doc = docx.Document(file_input)
                
            paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
            # Tablolardaki metinleri de al
            for table in doc.tables:
                for row in table.rows:
                    for cell in row.cells:
                        if cell.text.strip():
                            paragraphs.append(cell.text.strip())
            return "\n".join(paragraphs).strip()
        except Exception as e:
            return f"DOCX Okuma Hatası: {str(e)}"

    @staticmethod
    def extract_from_txt(file_input):
        """
        Düz metin (.txt) dosyalarını veya ham metin girdilerini okur.
        """
        try:
            if isinstance(file_input, str):
                if os.path.exists(file_input):
                    with open(file_input, "r", encoding="utf-8", errors="ignore") as f:
                        return f.read().strip()
                return file_input.strip()
            else:
                content = file_input.read()
                if isinstance(content, bytes):
                    return content.decode("utf-8", errors="ignore").strip()
                return str(content).strip()
        except Exception as e:
            return f"Metin Okuma Hatası: {str(e)}"

    @classmethod
    def parse(cls, file_input, filename=None):
        """
        Dosya uzantısına göre en uygun okuyucuyu otomatik seçer.
        """
        if filename is None and isinstance(file_input, str):
            filename = file_input
        elif filename is None and hasattr(file_input, "name"):
            filename = file_input.name
        else:
            filename = str(filename or "file.txt")

        ext = os.path.splitext(filename)[1].lower()

        if ext == ".pdf":
            return cls.extract_from_pdf(file_input)
        elif ext in [".docx", ".doc"]:
            return cls.extract_from_docx(file_input)
        else:
            return cls.extract_from_txt(file_input)

if __name__ == "__main__":
    test_text = "Sample CV content with Python and Machine Learning."
    result = CVParser.extract_from_txt(test_text)
    print("CVParser hazır, test çıktısı:", result)
