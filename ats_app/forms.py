import os
from django import forms
from .models import Job, Applicant

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 10}),
        }

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'email', 'resume']
        widgets = {
            'resume': forms.ClearableFileInput(attrs={'accept': '.pdf,.doc,.docx'})
        }

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            # Basic validation for file extension
            ext = os.path.splitext(resume.name)[1].lower()
            valid_extensions = ['.pdf', '.doc', '.docx']
            if ext not in valid_extensions:
                raise forms.ValidationError("Unsupported file type. Please upload a PDF, DOC, or DOCX file.")
            # Optional: Add file size validation
            # if resume.size > 5 * 1024 * 1024: # 5MB limit
            #     raise forms.ValidationError("File size cannot exceed 5MB.")
        return resume