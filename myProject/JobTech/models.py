from django.db import models

class Job(models.Model):
    title = models.CharField(
        max_length=75,
        verbose_name="Job Title",
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name="Job Description",
        help_text="Detailed job description",
        null=True,
        blank=True,
    )
    responsibility = models.TextField(
        verbose_name="Job Responsibility ",
        help_text="Detailed job responsibilities",
        null=True,
        blank=True,
    )
    qualifications  = models.TextField(
        verbose_name="Job Qualifications ",
        help_text="Detailed job qualifications",
        null=True,
        blank=True,
    )
    MinSalary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Min Salary "
    )
    MaxSalary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Max Salary Amount"
    )
    CATEGORIES = [
        ('IT Services & Consulting', 'IT Services & Consulting'),
        ('Marketing', 'Marketing'),
        ('Customer Service', 'Customer Service'),
        ('Human Resource', 'Human Resource'),
        ('Project Management', 'Project Management'),
        ('Business Development', 'Business Development '),
        ('Sales & Communication', 'Sales & Communication'),
        ('Teaching & Education', 'Teaching & Education'),
        ('Design & Creative', 'Design & Creative'),
    ]
    category = models.CharField(
        max_length=75,
        choices=CATEGORIES,
        default='office',
        verbose_name="Category"

    )
    REMOTE_CHOICES = [
        ('Remote', 'Fully Remote'),
        ('Hybrid', 'Partially Remote'),
        ('On Site', 'Office Based'),
    ]
    remote = models.CharField(
        max_length=20,
        choices=REMOTE_CHOICES,
        default='office',
        verbose_name="Remote Work Option"
    )
    location = models.CharField(  
        max_length=255,
        verbose_name="Job Location"
    )
    img = models.ImageField(
        default='fallback.png',
        blank=True,
        null=True,
        verbose_name="Job Image"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Posting Date"
    )

    def __str__(self):
        return self.title

