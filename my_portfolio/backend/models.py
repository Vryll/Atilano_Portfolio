from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

class User(AbstractUser):
    image_profile=models.ImageField(upload_to='image_profile/', null=True, blank=True)
    first_name=models.CharField(max_length=200, null = True, blank = True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name=models.CharField(max_length=200, null = True, blank=True)
    contact_number=models.CharField(max_length=200, null = True, blank=True)
    age = models.CharField(max_length=200, null = True, blank=True)
    address = models.CharField(max_length=200, null = True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    facebook_link=models.CharField(max_length=200, null = True, blank=True)
    github_link=models.CharField(max_length=200, null = True, blank=True)
    linkedin_link=models.CharField(max_length=200, null = True, blank=True)
    username = models.CharField(max_length=150,null = True, blank=True, unique=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    confirm_password = models.CharField(max_length=200, null=True, blank=True)
    about_me_context=models.CharField(max_length=500, null = True, blank = True)
    resume=models.FileField(upload_to='resume/', null = True, blank=True)

    def __str__(self):
        return self.email or str(self.id)
    
class Skill(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True, related_name="skill")
    skill_logo = models.ImageField(upload_to='skill_logo/', null=True, blank=True)
    skill_name = models.CharField(max_length=200, null = True, blank = True)

    # def __str__(self):
    #     return self.skill_name
    
class Project(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True, related_name="project")
    project_profile = models.ImageField(upload_to='project_profile/', null=True, blank=True)
    project_title = models.CharField(max_length=250, null = True, blank = True)
    project_content = models.CharField(max_length=500, null = True, blank = True)
    project_posted_date = models.DateTimeField(null=True, blank=True, default=datetime.today())

    def __str__(self):
        return self.project_title

class ProjectImage(models.Model):
    project_id=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_img")
    project_image=models.ImageField(upload_to='project_img/', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.project.project_title}"
    

    

