
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseServerError
from .models import Job, Applicant
from .forms import JobForm, ApplicantForm
from django.conf import settings
import os


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import docx 


def extract_text_from_file(file_path):
 
    text = ""
    try:
        _, extension = os.path.splitext(file_path)
        extension = extension.lower()

        if extension == '.pdf':
            try:
                with open(file_path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        page_text = page.extract_text()
                        if page_text: 
                            text += page_text + "\n"
            except Exception as e:
                print(f"Error reading PDF {file_path}: {e}")
                # Fallback or specific handling if needed
                text = "" # Ensure text is empty on error

        elif extension == '.docx':
            try:
                doc = docx.Document(file_path)
                for para in doc.paragraphs:
                    text += para.text + "\n"
            except Exception as e:
                print(f"Error reading DOCX {file_path}: {e}")
                text = ""

        elif extension == '.doc':
            
            print(f"Skipping .doc file (not directly supported): {file_path}")
            text = "" 
        
        text = ' '.join(text.split()) 

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return ""

    return text


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'ats_app/login.html', {'error': 'Invalid username or password.'})

    return render(request, 'ats_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def home(request):
    return render(request, 'ats_app/home.html')

def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'ats_app/job_form.html', {'form': form})

def job_list(request):
    jobs = Job.objects.order_by('-posted_date')
    return render(request, 'ats_app/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'ats_app/job_detail.html', {'job': job})

def upload_resume(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('applicant_list')
    else:
        form = ApplicantForm()
    return render(request, 'ats_app/applicant_form.html', {'form': form})

def applicant_list(request):
    applicants = Applicant.objects.order_by('-uploaded_date')
    return render(request, 'ats_app/applicant_list.html', {'applicants': applicants})

def find_matches(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    applicants = Applicant.objects.all()

    if not applicants:
        return render(request, 'ats_app/match_results.html', {'job': job, 'ranked_applicants': [], 'error': 'No applicants found.'})

    job_description = job.description
    resume_texts = []
    valid_applicants = [] 

    for applicant in applicants:
        if applicant.resume:
            file_path = os.path.join(settings.MEDIA_ROOT, applicant.resume.name)
            if os.path.exists(file_path):
                text = extract_text_from_file(file_path)
                if text is not None: 
                    resume_texts.append(text if text else "") 
                    valid_applicants.append(applicant)
                else:
                    print(f"Warning: Could not find or read resume file for {applicant.name}: {file_path}")
            else:
                 print(f"Warning: Resume file path does not exist for {applicant.name}: {file_path}")
        else:
            print(f"Warning: Applicant {applicant.name} has no resume file associated.")


    if not valid_applicants or not any(resume_texts): 
         return render(request, 'ats_app/match_results.html', {
             'job': job,
             'ranked_applicants': [],
             'error': 'Could not extract text from any resumes or no valid resumes found.'
         })


   
    try:
        
        documents = [job_description] + resume_texts

        
        documents = [doc if doc else " " for doc in documents]

        vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)

        if not documents or all(not doc.strip() for doc in documents):
             return render(request, 'ats_app/match_results.html', {
                 'job': job,
                 'ranked_applicants': [],
                 'error': 'No text content found in job description or resumes to perform matching.'
             })

        tfidf_matrix = vectorizer.fit_transform(documents)

       
        cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

       
        if len(valid_applicants) == cosine_similarities.shape[1]:
            scores = cosine_similarities.flatten()
            applicant_scores = list(zip(valid_applicants, scores))

        
            ranked_applicants = sorted(applicant_scores, key=lambda x: x[1], reverse=True)

        
            ranked_applicants_formatted = [
                (applicant, f"{score*100:.2f}%") for applicant, score in ranked_applicants
            ]
        else:
            
             print(f"Error: Mismatch between number of valid applicants ({len(valid_applicants)}) and calculated scores ({cosine_similarities.shape[1]})")
             return render(request, 'ats_app/match_results.html', {
                 'job': job,
                 'ranked_applicants': [],
                 'error': 'Internal error: Mismatch during similarity calculation.'
             })


    except ValueError as e:
        
         print(f"TF-IDF Error: {e}")
         return render(request, 'ats_app/match_results.html', {
             'job': job,
             'ranked_applicants': [],
             'error': f'Could not perform matching. TF-IDF Error: {e}'
         })
    except Exception as e:
    
        print(f"Error during matching process: {e}")
   
        return HttpResponseServerError("An unexpected error occurred during the matching process.")


    return render(request, 'ats_app/match_results.html', {
        'job': job,
        'ranked_applicants': ranked_applicants_formatted
    })





