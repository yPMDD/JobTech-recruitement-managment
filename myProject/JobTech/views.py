from django.shortcuts import render
from .models import Job 
# Create your views here.

def homepage(req):
    Jobs  = Job.objects.all().order_by('-date')
    return render(req,'index.html',{'jobs': Jobs})

def about(req):
    return render(req,'about.html')

def notfound(req):
    return render(req,'404.html')
def contact(req):
    return render(req,'contact.html')

def category(req):
    return render(req,'category.html')

def jobList(req):
    return render(req,'job-list.html')

def jobDetail(req):
    return render(req,'job-detail.html')

def testimonial(req):
    return render(req,'testimonial.html')