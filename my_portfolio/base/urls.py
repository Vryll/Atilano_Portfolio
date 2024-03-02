from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path ('', views.home, name='index'),
    path ('admin_cms/admin_home/', views.adminCms, name='admin_home'),
    path ('admin_cms/personal_information/', views.admin_personal_info, name='personal_information'),
    path ('admin_cms/skills/', views.admin_skills, name='admin_skills'),
    path ('admin_cms/projects/', views.admin_projects, name="admin_projects")
]