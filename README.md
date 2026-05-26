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

## 🛠️ Tech Stack & Dependencies

* **Backend Framework:** Django (Python)
* **Frontend:** HTML5, CSS3, Bootstrap (Fully Responsive)
* **Database:** SQLite (Default / Development) — easily migratable to PostgreSQL/MySQL.
* **AI/NLP Layer:** Python Natural Language Processing libraries (such as `spaCy`, `NLTK`, or LLM integrations) for parsing and matching algorithms.

---

## 📁 Project Structure

```text
Ats_Application/
│
├── ats_app/                # Main application logic
│   ├── migrations/         # Database migration files
│   ├── static/             # CSS styles, JavaScript, and UI assets
│   ├── templates/          # HTML interfaces for Recruiters and Candidates
│   │   ├── base.html       # Global boilerplate layout
│   │   ├── recruiter/      # Dashboards, job creation forms, candidate ranking lists
│   │   └── candidate/      # Job boards, application status portals
│   ├── admin.py            # Admin panel registration
│   ├── apps.py             # Application configuration
│   ├── forms.py            # Form validation logic (Job post form, Candidate application form)
│   ├── models.py           # Database schemas (Job, Candidate, Profile, Application)
│   ├── views.py            # Business logic controllers
│   └── urls.py             # App-specific routing paths
│
├── myats_project/          # Project configuration directory
│   ├── settings.py         # Global settings (Installed apps, Middleware, Databases)
│   ├── urls.py             # Global routing definitions
│   └── wsgi.py / asgi.py   # Server gateway entrypoints
│
├── media/                  # Media root folder
│   └── resumes/            # Securely stored candidate resumes (PDFs/Docs)
│
├── manage.py               # Django project manager CLI
└── db.sqlite3              # Local development database
