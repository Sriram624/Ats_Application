from django.db import models
from django.utils import timezone
import os

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# Function to define upload path for resumes
def resume_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/resumes/<applicant_name>_<filename>
    # Sanitize filename if needed
    sanitized_name = "".join(c if c.isalnum() or c in ['.', '_'] else '_' for c in instance.name)
    return os.path.join('resumes', f"{sanitized_name}_{filename}")

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Use the function to determine upload path
    resume = models.FileField(upload_to=resume_upload_path)
    uploaded_date = models.DateTimeField(default=timezone.now)
    # Optional: Store extracted text to avoid re-processing?
    # resume_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

    # Optional: Add a method to get the filename
    def filename(self):
        return os.path.basename(self.resume.name)
