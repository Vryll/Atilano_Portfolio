from django.shortcuts import redirect, render
from backend.forms import *
from backend.models import *
 
# Create your views here.
def home(request):
    return render(request, 'index.html')

def navBar(request):
    return render(request, 'navbar.html')

def adminCms(request):
    return render(request, 'admin_cms.html')

def admin_personal_info(request):
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../templates/personal_information.html')
    else:
        form = PersonalInformationForm()

    context = {'form': form}
    return render(request, 'personal_information.html', context)


def admin_skills(request):
    if request.method == 'POST':
        form = SkillsForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("skill_name")
            skill_instance = Skill.objects.create(skill_logo=request.FILES.get("skill_logo", None), skill_name=name)
            print(skill_instance)
            print(request.FILES.get("skill_logo", None))
            return redirect('base:admin_skills')
        else:
            print(form.errors)
    else:
        form = SkillsForm()

    context = {'form': form}
    return render(request, 'skills.html', context)



def admin_projects(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project_name = form.cleaned_data.get("project_title")
            project_overview = form.cleaned_data.get("project_content")

            project_instance = Project.objects.create(
                project_img = request.FILES.get("project_img", None), 
                project_title = project_name,
                project_content = project_overview,
            )
            print(project_instance)
            print(request.FILES.get("project_img", None))
            return redirect('base:admin_projects')
        else:
            print(form.errors)
    else:
        form = ProjectForm()
    
    context = {'form': form}
    return render(request, 'admin-projects.html', context)