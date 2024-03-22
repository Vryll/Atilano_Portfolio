from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path ('', views.home, name='index'),
    path('login_page/', views.login, name='login_page'),
    path ('admin_cms/admin_home/', views.adminCms, name='admin_home'),
    path ('admin_cms/personal_information/', views.admin_personal_info, name='personal_information'),
    path ('admin_cms/skills/', views.admin_skills, name='admin_skills'),
    path('admin_cms/get_skills/',views.getSkill,name="get_skills"),
    path('admin_cms/delete_skills/', views.delSkill, name="delete_skills"),
    path ('admin_cms/projects/', views.admin_projects, name="admin_projects"),
    path ('admin_cms/get_projects/', views.getProject, name="get_admin_projects"),
    path ('admin_cms/delete_projects/', views.delProject, name="delete_projects"),
    path ('admin_cms/user_profile', views.userProfile, name="user_profile")
]