# AI-Powered Applicant Tracking System (ATS)

A web-based Applicant Tracking System (ATS) built with Django and scikit-learn. This system allows recruiters to post job openings, accept candidate resume uploads (PDF & DOCX), and automatically score and rank applicants using natural language processing (TF-IDF & Cosine Similarity).

---

## 🚀 Features

* **Job Management:** Post, list, and view detailed job openings.
* **Resume Parsing:** Automatically extracts text content from uploaded .pdf and .docx resumes.
* **AI Resume Matching:** Compares raw resume text against the job description using scikit-learn to generate an instant match percentage (0% to 100%).
* **Candidate Ranking:** Displays applicants ranked from highest to lowest match score for easy screening.
* **Authentication:** Simple user session management (Login/Logout) to secure recruiter actions.

---

## 🛠️ Tech Stack

* **Backend Framework:** Django (Python)
* **Text Extraction:** PyPDF2 & python-docx
* **Machine Learning Layer:** scikit-learn (TfidfVectorizer & cosine_similarity)
* **Database:** SQLite (Default development database)

---

## 📁 Project Layout

Ats_Application/
│
├── ats_app/                # Core application directory
│   ├── templates/          # HTML files (job forms, applicant lists, match results)
│   ├── models.py           # Database schemas (Job, Applicant)
│   ├── views.py            # Logic for text parsing and TF-IDF matching
│   └── urls.py             # App routing paths
│
├── myats_project/          # Project configuration folder
├── media/resumes/          # Directory where uploaded resumes are securely stored
├── manage.py               # Django CLI management tool
└── db.sqlite3              # Local database file

---

## ⚙️ Installation & Setup

### 1. Clone the Project
git clone https://github.com/Sriram624/Ats_Application.git
cd Ats_Application

### 2. Set Up a Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

### 3. Install Required Packages
pip install django scikit-learn PyPDF2 python-docx

### 4. Run Migrations & Create User
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

### 5. Launch the Application
python manage.py runserver

Open your web browser and go to http://127.0.0.1:8000/

---

## 📄 License

Distributed under the MIT License. See LICENSE for details.
