# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    ROLE_CHOICES = (
        ('recruiter', 'Recruiter'),
        ('candidate', 'Candidate'),
        ('HR services', 'HR services'),
    )
    email = models.EmailField(unique=True, max_length=191)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    def __str__(self):
        return self.get_full_name()
