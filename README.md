# AI-Powered Applicant Tracking System (ATS)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A web-based **Applicant Tracking System (ATS)** built with **Django** and integrated with **Artificial Intelligence** to streamline the modern hiring process. This application empowers recruiters to effortlessly post job openings, manage incoming applications, and leverage intelligent, automated resume parsing and ranking to identify top talent in seconds.

---

## 🚀 Features

### For Recruiters
* **Job Management:** Create, update, and archive job listings with detailed descriptions, required skills, and experience levels.
* **AI-Driven Resume Parsing:** Automatically extract key information (skills, education, work experience, contact details) from uploaded PDF/Word resumes.
* **Smart Ranking Dashboard:** Automatically score and rank candidates against specific job descriptions using NLP/AI semantic matching.
* **Application Pipeline:** Track candidates through various stages of the hiring funnel (e.g., Applied, Shortlisted, Interviewed, Hired/Rejected).

### For Candidates
* **Job Board Explorer:** Browse open positions with filtering options.
* **Seamless Application Process:** Apply to targeted positions with quick form-fills and resume upload capabilities.
* **Application Tracking:** View the real-time status of submitted applications via a personalized user dashboard.

---

## 🛠️ Tech Stack

* **Backend Framework:** Django (Python)
* **Frontend:** HTML5, CSS3, Bootstrap (Fully Responsive)
* **Database:** SQLite (Default / Development) — easily migratable to PostgreSQL/MySQL.
* **AI/NLP Layer:** Python Natural Language Processing libraries (such as `spaCy`, `NLTK`, or LLM integrations) for parsing and matching algorithms.

---

## 📁 Project Structure

```text
Ats_Application/
│
├── ats_app/                # Main application logic (Views, Models, Templates, Forms)
│   ├── templates/          # HTML interfaces for Recruiters and Candidates
│   ├── static/             # CSS styles, JavaScript, and UI assets
│   └── ...
│
├── myats_project/          # Project configuration directory (settings.py, urls.py)
│
├── media/                  # Media root folder
│   └── resumes/            # Securely stored candidate resumes (PDFs/Docs)
│
├── manage.py               # Django project manager CLI
└── db.sqlite3              # Local development database
⚙️ Installation & Setup
Follow these steps to get your local development environment up and running.

1. Prerequisites
Ensure you have Python 3.8+ and pip installed on your machine.

2. Clone the Repository
Bash
git clone [https://github.com/Sriram624/Ats_Application.git](https://github.com/Sriram624/Ats_Application.git)
cd Ats_Application
3. Create a Virtual Environment
Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
4. Install Dependencies
(Note: Ensure you generate a requirements.txt if you haven't already by running pip freeze > requirements.txt after installing your packages.)

Bash
pip install -r requirements.txt
5. Run Database Migrations
Bash
python manage.py makemigrations
python manage.py migrate
6. Create a Superuser (Recruiter/Admin Access)
Bash
python manage.py createsuperuser
7. Launch the Development Server
Bash
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/.
