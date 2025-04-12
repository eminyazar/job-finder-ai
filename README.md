# 🧠 Job Finder AI

A smart CV analyzer and job recommender system powered by FastAPI and Streamlit.

## 🚀 Overview

Job Finder AI helps users upload their CVs (in PDF or DOCX format), extract relevant skills using NLP, and get personalized job recommendations. It also provides direct job search links on LinkedIn based on matched job titles.

## 🛠 Tech Stack

- 🐍 **Python 3.12+**
- ⚡ **FastAPI** – Backend API
- 🎈 **Streamlit** – Frontend UI
- 🤖 **spaCy** – Skill extraction with NLP
- 📄 **pdfplumber / python-docx** – Text extraction from CVs
- 🌐 **Requests** – API communication
- 💼 **LinkedIn Job Links** – Job search redirection

---

## 📷 Demo

![Ekran görüntüsü 2025-04-13 004252](https://github.com/user-attachments/assets/863c789d-e430-4ff2-ab02-86785d347d6c)
![Ekran görüntüsü 2025-04-13 004333](https://github.com/user-attachments/assets/e54d2488-9493-42c1-b39a-de6d41605191)

---

## 💡 Features

- Upload CV in `.pdf` or `.docx` format
- Extracts key skills using NLP
- Recommends jobs based on skill matches
- Highlights common skills per job
- Direct link to search those jobs on LinkedIn

---

## 📦 Installation

1. **Clone the repo**  

git clone https://github.com/eminyazar/job-finder-ai.git
cd job-finder-ai

python -m venv venv
venv\Scripts\activate  # On Windows

pip install -r requirements.txt

cd app
uvicorn main:app --reload

streamlit run frontend.py

---

🔍 Example Output

{
  "skills": ["python", "sql"],
  "recommended_jobs": [
    {
      "job": "data scientist",
      "common_skills": ["python", "sql"]
    },
    {
      "job": "backend developer",
      "common_skills": ["python", "sql"]
    }
  ]
}

---

📬 Contact

Connect on: https://www.linkedin.com/in/emin-yazar-127523257/
