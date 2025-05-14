from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404,redirect

from .forms import CustomUserCreationForm, CustomLoginForm ,EditProfileForm,EditProfilePicture
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser


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



@login_required(login_url='/users/login')
def editProfile(request,id):
    User = get_object_or_404(CustomUser, id=id)
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=User)
         # Make picture field optional
          # Debugging
        if form.is_valid():

            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('users:profile')
        else:
            messages.error(request, "Please correct the errors below")
            print("Form errors:", form.errors)  # Debugging
    else:
        form = EditProfileForm(instance=User)
    
    return render(request, 'profile.html', {
        'form': form,
        'User': User
    })

@login_required(login_url='/users/login')
def editProfilePicture(request, id):
    user = get_object_or_404(CustomUser, id=id)

    if request.method == 'POST':
        form = EditProfilePicture(request.POST, request.FILES, instance=user)
        if 'email' in form.fields:
            form.fields['email'].required = False
        if form.is_valid():
            form.save()
            messages.success(request, "Profile picture updated successfully")
            return redirect('users:profile')  # make sure this URL name exists
        else:
            messages.error(request, "Please correct the errors below")
            print("Form errors:", form.errors)
    else:
        form = EditProfilePicture(instance=user)
        if 'email' in form.fields:
            form.fields['email'].required = False

    return render(request, 'profile.html', {
        'form': form,
        'User': user
    })

@login_required(login_url='/users/login')
def deleteProfile(request, id):
    User = get_object_or_404(CustomUser, id=id)
    
    if request.method == 'POST':
        User.delete()
        
        messages.success(request, "Profile deleted successfully")
        return redirect('home')
    
    return render(request, 'profile.html', {
        'User': User
    })


 