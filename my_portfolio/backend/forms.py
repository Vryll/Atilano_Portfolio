from django.forms import ModelForm
from .models import *


class PersonalInformationForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class SkillsForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_logo', 'skill_name']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_title', 'project_content', 'project_img', 'project_posted_date']