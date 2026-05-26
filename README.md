# AI-Powered Applicant Tracking System (ATS)

An intelligent web-based Applicant Tracking System (ATS) built using Django and scikit-learn. The platform allows recruiters to create job postings, upload candidate resumes (PDF & DOCX), and automatically evaluate applicants using Natural Language Processing (NLP) techniques such as TF-IDF Vectorization and Cosine Similarity.

The system streamlines the hiring process by ranking candidates based on how closely their resumes match the job description.

---

# Features

## Job Management
- Create and manage job openings
- View detailed job descriptions
- Organize applicants for each role

## Resume Parsing
- Supports PDF and DOCX resume uploads
- Automatically extracts text content from resumes
- Handles multiple candidate submissions efficiently

## AI Resume Matching
- Uses TF-IDF Vectorization and Cosine Similarity
- Compares resumes against job descriptions
- Generates a match score from 0% to 100%

## Candidate Ranking
- Automatically ranks applicants based on match percentage
- Helps recruiters identify top candidates quickly
- Simplifies the shortlisting process

## Authentication System
- Secure recruiter login and logout functionality
- Protected recruiter actions and applicant management

---

# Tech Stack

| Category | Technology |
|---|---|
| Backend Framework | Django |
| Programming Language | Python |
| Machine Learning | scikit-learn |
| NLP Techniques | TF-IDF Vectorization, Cosine Similarity |
| Resume Parsing | PyPDF2, python-docx |
| Database | SQLite |
| Frontend | HTML, CSS |

---

# Project Structure

```bash
Ats_Application/
│
├── ats_app/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── myats_project/
│
├── media/
│   └── resumes/
│
├── manage.py
├── db.sqlite3
└── README.md
```

---

# Installation and Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Sriram624/Ats_Application.git
cd Ats_Application
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install django scikit-learn PyPDF2 python-docx
```

## 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 5. Create an Admin User

```bash
python manage.py createsuperuser
```

## 6. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```bash
http://127.0.0.1:8000/
```

---

# How the AI Matching Works

1. Extracts text from uploaded resumes
2. Cleans and processes textual content
3. Converts text into TF-IDF vectors
4. Computes Cosine Similarity between:
   - Job Description
   - Candidate Resume
5. Generates a relevance score
6. Ranks applicants from highest to lowest match score

---

# Author

Sriram B  
Software Developer | Backend Developer | AI Enthusiast
