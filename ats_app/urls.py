from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('post-job/', views.post_job, name='post_job'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('upload-resume/', views.upload_resume, name='upload_resume'),
    path('applicants/', views.applicant_list, name='applicant_list'),
    path('jobs/<int:job_id>/matches/', views.find_matches, name='find_matches'),
]
