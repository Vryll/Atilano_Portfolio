from django.forms import ModelForm
from .models import *


class PersonalInformationForm(ModelForm):
    class Meta:
        model = User
        fields = [
                'image_profile',
                'first_name', 
                'middle_name', 
                'last_name', 
                'contact_number',
                'age',
                'address',
                'email', 
                'facebook_link', 
                'github_link',
                'linkedin_link',
                'username',
                'password', 
                'confirm_password', 
                'about_me_context', 
                'resume'
            ]


class SkillsForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
                'skill_logo', 
                'skill_name'
            ]

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
                'project_profile',
                'project_title', 
                'project_content', 
                'project_posted_date'
            ]
        

class ProjectImageForm(ModelForm):
    class Meta:
        model = ProjectImage
        fields = [
                'project_image'
            ]