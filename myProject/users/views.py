from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib import messages

# Create your views here.
def user_login(req):
    next_url = req.GET.get('next', '')
    if next_url:  
        messages.warning(req, "Please log in first")
    if req.method == 'POST':
        form = CustomLoginForm(req.POST)
        if form.is_valid():
            user = form.get_user() 
            login(req, user)        
            messages.success(req, f'Welcome back , {user.username} !')
            return redirect('home') 
    else:
        form = CustomLoginForm()
    return render(req, 'login.html', {'form': form})

def signup(req):
    if req.method == 'POST':
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            messages.success(req,f'Welcome {user.username} , please head out to your profile to complete your registration ! ')
            return redirect('home')  
    else:
        form = CustomUserCreationForm()
    return render(req, 'signup.html', {'form': form})

def logout_view(req):
     if req.method == "POST": 
        logout(req) 
        messages.success(req,'You have been logged out !')
        return redirect("home")
     
def profile(req):
    return render(req,'profile.html')