from django.urls import path
from portfolio_pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("portfolio/", views.portfolio, name='portfolio'),
    path("portfolio/skills/",views.skills, name='skills'),
    path("portfolio/experience/",views.ExperienceList.as_view(), name='experience'),
    path("portfolio/project/", views.ProjectList.as_view(), name='project'),
    path("contacts/", views.contact, name='contact'),
    path('portfolio/projects/add/',views.project_create, name='create'),
    path('portfolio/projects/update<int:project_index>/', views.project_update, name='update'),
    path('portfolio/project/delete/<int:project_index>/', views.project_delete, name='delete'),
    path('portfolio/experience/update<int:experience_index>',views.experience_update,name='update_e'),
    path('portfolio/experience/delete<int:experience_index>',views.experience_delete,name='delete_e'),
    path('portfolio/experience/add',views.experience_create, name='create_e')
]