from django.shortcuts import redirect, render, get_object_or_404
from backend.forms import *
from backend.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request, 'login_page.html')

def home(request):
    try:
        user = User.objects.all()
        skill = Skill.objects.all()
        project = Project.objects.all()
        print(user)
    except User.DoesNotExist:
        return render(request, 'error.html', {'error_message': "User not found"})
    
    context = {'user': user, 'skill':skill, 'project':project}
    return render(request, 'index.html', context)

def navBar(request):
    return render(request, 'navbar.html')

@login_required(login_url="/auth/login")
def adminCms(request):
    return render(request, 'admin_cms.html')

@login_required(login_url="/auth/login")
def userProfile(request):
    return render(request, 'profile.html')

#CREATE
@login_required(login_url="/auth/login")
def admin_personal_info(request):
    user = User.objects.all()


    if request.method == 'POST':
        user_instance = request.user
        form = PersonalInformationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                cleaned_data = form.cleaned_data
                for field, value in cleaned_data.items():
                    if value:
                        setattr(user_instance, field, value)
                        user_instance.save()
                return redirect('base:personal_information')
            except Exception as e:
                print(f"Error: {e}")
                context = {'form': form, 'error_message': "There was a problem saving the data. Please try again."}
        else:
            print(form.errors)
    else:
        form = PersonalInformationForm()

    context = {'form': form, 'user': user}
    return render(request, 'personal_information.html', context)


@login_required(login_url="/auth/login")
def admin_skills(request):
    if request.method == 'POST':
        if request.POST.get('skill_id'):
            instance = Skill.objects.get(id = request.POST.get('skill_id'))
            skillForm = SkillsForm(request.POST, request.FILES, instance = instance)
        else:
            skillForm = SkillsForm(request.POST, request.FILES)
         

        if skillForm.is_valid():
            skillForm.save()
            return redirect('base:get_skills')
    else:
        skillForm = SkillsForm()
    return redirect('base:get_skills')

@login_required(login_url="/auth/login")
def admin_projects(request):
    if request.method == 'POST':
        if request.POST.get('project_id'):
            instance = Project.objects.get(id = request.POST.get('project_id'))
            project_form = ProjectForm(request.POST, request.FILES, instance = instance)
            project_img_form = ProjectImageForm(request.POST, request.FILES, instance=instance)
        else:
            project_form = ProjectForm(request.POST, request.FILES)
            project_img_form = ProjectImageForm(request.POST, request.FILES)

        if project_form.is_valid() and project_img_form.is_valid():
            project_instance = project_form.save()

            for project_image in request.FILES.getlist('project_image'):
                try:
                    ProjectImage.objects.create(project_id=project_instance, project_image=project_image)
                except Exception as e:
                    print(request, f"Error uploading image: {e}") 
            return redirect('base:get_admin_projects')
        else:
            print(request, project_form.errors, project_img_form.errors)
    else:
        project_form = ProjectForm()
        project_img_form = ProjectImageForm()
        
    return redirect('base:get_admin_projects')


#DELETE
@login_required(login_url="/auth/login")
def delSkill(request):
    if request.method == 'POST':
        skill_id = request.POST.get('skill_id')
        if skill_id:
            try:
                instance = Skill.objects.get(id = skill_id)
                instance.delete()
                print('successfully deleted')
                return redirect('base:get_skills')
            except Exception as e:
                print(request, f"An error occurred: {e}")
    return render(request, 'base:get_skills')

@login_required(login_url="/auth/login")
def delProject(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        if project_id:
            try:
                instance = Project.objects.get(id = project_id)
                instance.delete()
                print('successfully deleted')
                return redirect('base:get_admin_projects')
            except Exception as e:
                print(request, f"An error occurred: {e}")
        
    return render(request, 'base:get_admin_projects')


#GET FUNCTION
@login_required(login_url="/auth/login")
def getSkill(request):
    skill = Skill.objects.all()
    context = {'skill':skill}
    return render(request, 'skills.html', context)

@login_required(login_url="/auth/login")
def getProject(request):
    project= Project.objects.all()
    context = {'project': project}
    return render(request, 'admin-projects.html', context)








