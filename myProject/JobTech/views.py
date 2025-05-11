from django.shortcuts import render, get_object_or_404,redirect
from .models import Job 
from django.contrib.auth.decorators import login_required
from .forms import JobPostingForm
from django.contrib import messages

def homepage(req):
    Jobs  = Job.objects.all().order_by('-date')
    # messages.error(req,'error')
    # messages.success(req,'sucess')
    # messages.warning(req,'warning')
    return render(req,'index.html',{'jobs': Jobs})

def about(req):
    return render(req,'about.html')

def notfound(req):
    return render(req,'404.html')
def contact(req):
    return render(req,'contact.html')

def category(req):
    return render(req,'category.html')

@login_required(login_url='/users/login')
def jobList(req):
    Jobs  = Job.objects.all().order_by('-date')
    return render(req,'job-list.html',{'jobs': Jobs})

def jobDetail(req):
    return render(req,'job-detail.html')

def testimonial(req):
    return render(req,'testimonial.html')


@login_required(login_url='/users/login')
def jobDetails(req, id):
    job = get_object_or_404(Job, id=id)
    return render(req, 'job-detail.html', {'job': job})

@login_required(login_url='/users/login')
def jobForm(req):
    if req.method == 'POST':
        form = JobPostingForm(req.POST)
        print(form.errors)  # Before is_valid()
        if form.is_valid():
                
                # Create Job instance manually
                job = Job(
                    title=form.cleaned_data['title'],
                    contact_email=form.cleaned_data['contact_email'],
                    MinSalary=form.cleaned_data['MinSalary'],
                    MaxSalary=form.cleaned_data['MaxSalary'],
                    category=form.cleaned_data['category'],
                    remote=form.cleaned_data['remote'],
                    location=form.cleaned_data['location'],
                    description=form.cleaned_data['description'],
                    responsibility=form.cleaned_data['responsibility'],
                    qualifications=form.cleaned_data['qualifications'],
                    poster=req.user
                )
                job.save()
                messages.success(req,'Job Posted Successfully !')
                return redirect('home')  
    else:
        
        form = JobPostingForm()

    return render(req, 'jobForm.html', {'form': form})

@login_required(login_url='/users/login')
def jobsPosted(req):
    Jobs  = Job.objects.all().order_by('-date')
    return render(req,'jobsPosted.html',{'jobs':Jobs})


@login_required(login_url='/users/login')
def editJob(request, id):
    job = get_object_or_404(Job, id=id, poster=request.user)
    
    if request.method == 'POST':
        form = JobPostingForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job updated successfully")
            return redirect('jobsPosted')
        else:
            messages.error(request, "Please correct the errors below")
            print("Form errors:", form.errors)  # Debugging
    else:
        form = JobPostingForm(instance=job)
    
    return render(request, 'editJob.html', {
        'form': form,
        'job': job
    })

def deleteJob(req,id):
    job = get_object_or_404(Job, id=id, poster=req.user)  # Ensure only owner can delete
    job.delete()
    messages.success(req, "Job deleted successfully")
    return redirect('jobsPosted')  # Redirect to jobs list page