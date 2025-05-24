from django.shortcuts import render, get_object_or_404,redirect
from .models import Job , Application
from django.contrib.auth.decorators import login_required
from .forms import JobPostingForm
from django.contrib import messages
from django.contrib.auth.models import User

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




@login_required(login_url='/users/login')
def applyJob(request, id):
    job = get_object_or_404(Job, id=id)
    
    if request.method == 'POST':
        # Check if the user has already applied for this job
        if Application.objects.filter(job=job, applicant=request.user).exists():
            messages.error(request, "You have already applied for this job.")
            return redirect('home')
        job.applications = job.applications + 1
        job.save()

        if request.user.candidate.resume is None:
            messages.error(request, "Please upload your resume before applying.")
            return redirect('profile')
        
        app = Application(
            job=job,
            applicant=request.user,
            cover_letter=request.user.candidate.cover_letter,
            resume=request.user.candidate.resume
            
        )
        
        app.save()
        # Handle the application logic here
        messages.success(request, f"You have successfully applied for the {job.title} job!")
        return redirect('home')
    
    return render(request, 'appliedJobs.html', {
        'user': User,
        'job': job
    })



def appliedJobs(request):
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'appliedJobs.html', {
        'applications': applications
    })

def viewApplicants(request, id):
    job = get_object_or_404(Job, id=id)
    applications = Application.objects.filter(job=job)
    return render(request, 'viewApplicants.html', {
        'applications': applications,
        'job': job
    })


def changeAppStatus(request, id, status):
    application = get_object_or_404(Application, id=id)
    
    if request.method == 'POST':
        application.status = status
        application.save()
        messages.success(request, f"Application status updated to {status}")
        return redirect('viewApplicants', id=application.job.id)
    
    return render(request, 'viewApplicants.html', {
        'application': application,
        'status': status
    })

def changeJobStatus(request, id, status):
    job = get_object_or_404(Job, id=id)
    
    if request.method == 'POST':
        job.status = status
        job.save()
        messages.success(request, f"Job status updated to {status}")
        return redirect('jobsPosted')
    
    return render(request, 'jobsPosted.html', {
        'job': job,
        'status': status
    })

def deleteApplication(request, id):
    application = get_object_or_404(Application, id=id)
    job = get_object_or_404(Job, id=application.job.id)
    if request.method == 'POST':
        job.applications = job.applications - 1
        job.save()
        application.delete()
        messages.success(request, "Application deleted successfully")
        return redirect('appliedJobs')
    
    return render(request, 'appliedJobs.html', {
        'application': application
    })