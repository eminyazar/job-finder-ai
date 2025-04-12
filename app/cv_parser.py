import PyPDF2
import docx
import spacy
from io import BytesIO

nlp = spacy.load("en_core_web_sm")

SKILL_KEYWORDS = [
    # Backend
    "python", "django", "fastapi", "flask", "node.js", "express.js", "php", "laravel",
    "java", "spring", "c#", ".net", "go", "rust",

    # Frontend
    "javascript", "typescript", "react", "vue", "angular", "next.js", "html", "css", "sass", "tailwind",

    # Mobile
    "flutter", "kotlin", "swift", "react native", "firebase",

    # Database
    "sql", "mysql", "postgresql", "mongodb", "redis", "oracle",

    # Data & AI
    "machine learning", "deep learning", "data analysis", "data visualization", "etl", "big data",
    "power bi", "tableau", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",

    # Cloud & DevOps
    "aws", "azure", "gcp", "docker", "kubernetes", "linux", "git", "github", "gitlab", "jenkins", "terraform",

    # Tools & Methodologies
    "api", "rest api", "graphql", "oop", "microservices", "cloud computing",
    "agile", "scrum", "jira", "ci/cd", "unit testing", "tdd",

    # Other Skills
    "excel", "communication", "problem solving", "teamwork", "leadership", "english"
]

def extract_text_from_pdf(file_content):
    file_content.seek(0)
    reader = PyPDF2.PdfReader(BytesIO(file_content.read()))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file_content):
    file_content.seek(0)
    doc = docx.Document(BytesIO(file_content.read()))
    return "\n".join([p.text for p in doc.paragraphs])

def extract_skills(file_content):
    try:
        text = extract_text_from_pdf(file_content)
    except Exception:
        text = extract_text_from_docx(file_content)

    doc = nlp(text.lower())
    extracted_skills = []

    for token in doc:
        if token.text in SKILL_KEYWORDS:
            extracted_skills.append(token.text)

    return list(set(extracted_skills))
