from django.urls import path
from . import views 



urlpatterns = [
    path('', views.homepage,name='home'),
    path('about/',views.about),
    path('notfound/',views.notfound),
    path('category/',views.category),
    path('contact/',views.contact),
    path('jobDetail/',views.jobDetail, name='jobDetail'),
    path('jobList/',views.jobList,name="jobList"),
    path('testimonial/',views.testimonial),
    path('jobForm/',views.jobForm),
    path('jobsPosted',views.jobsPosted,name="jobsPosted"),
    path('editJob/<int:id>/',views.editJob,name='editJob'),
    path('deleteJob/<int:id>/', views.deleteJob, name='deleteJob'),
    path('jobDetail/<int:id>/', views.jobDetails , name='jobDetails')
    
] 