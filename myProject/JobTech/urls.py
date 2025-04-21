from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homepage),
    path('about/',views.about),
    path('notfound/',views.notfound),
    path('category/',views.category),
    path('contact/',views.contact),
    path('jobDetail/',views.jobDetail),
    path('jobList/',views.jobList),
    path('testimonial/',views.testimonial),
    

    
    
]