# resume_reader.py
import os
from pathlib import Path

def extract_text(path):
    ext = Path(path).suffix.lower()
    if ext == ".pdf":
        return _read_pdf(path)
    elif ext == ".docx":
        return _read_docx(path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

def _read_pdf(path):
    import pdfplumber
    with pdfplumber.open(path) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)

def _read_docx(path):
    from docx import Document
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

# --- test it ---
text = extract_text(r"C:\Users\ashis\Downloads\Ashish.Kumar.pdf")
print(text[:1000])

from dotenv import load_dotenv
from groq import Groq
