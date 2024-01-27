from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView

from .models import Project,Experience

#this is for the normal pages
def home(request):
    return render(request, "portfolio_pages/home.html", {})


def portfolio(request):
    return render(request,"portfolio_pages/portfolio_list.html",{})

def skills(request):
    return render(request,"portfolio_pages/skills.html",{})

def experience(request):
    return render(request,"portfolio_pages/experience.html",{})


def contact(request):
    return render(request, "portfolio_pages/contacts.html",{})



#project views
class ProjectList(ListView):
    model= Project
    template_name = 'portfolio_pages/project.html'
    context_object_name = 'project_data'
    paginate_by = 2



def project_create(request):
    new_project = Project()

    if request.method == 'POST':
        new_project.title = request.POST.get('title', '')
        new_project.description = request.POST.get('description', '')
        new_project.credential = request.POST.get('credential', '')       
        new_project.save()
        return redirect('project')

    return render(request, 'portfolio_pages/add_project.html', context={'project': new_project})



def project_update(request, project_index):
    project_to_update = Project.objects.get(pk=project_index)

    if request.method == 'POST':
        project_to_update.title = request.POST['title']
        project_to_update.credential = request.POST['credential']
        project_to_update.description=request.POST['description']       
        project_to_update.save()
        return redirect('project')
    return render(request, 'portfolio_pages/update_project.html',context={'project':project_to_update})



def project_delete(request, project_index):
    project_to_delete = Project.objects.get(pk=project_index)
    if request.method == 'POST':
        project_to_delete.delete()
        return redirect('project')
    return render(request, 'portfolio_pages/delete_project.html', context={'project': project_to_delete})

#Experience views
def experience_create(request):
    new_experience = Experience()

    if request.method == 'POST':
        new_experience.category = request.POST.get('category', '')
        new_experience.organization = request.POST.get('organization', '')
        new_experience.role = request.POST.get('role', '')       
        new_experience.save()
        return redirect('experience')

    return render(request, 'experience_pages/add_experience.html', context={'experience': new_experience})


class ExperienceList(ListView):
    model = Experience
    template_name= 'experience_pages/experience.html'
    context_object_name = 'experience_data'
    paginate_by = 1

def experience_update(request, experience_index):
    experience_to_update = Experience.objects.get(pk=experience_index)

    if request.method == 'POST':
        print(request.POST)  # Add this line for debugging
        experience_to_update.category = request.POST['category']
        
        # Check if 'organization' key is present in request.POST before accessing it
        if 'organization' in request.POST:
            experience_to_update.organization = request.POST['organization']
            
        experience_to_update.role = request.POST['role']
        experience_to_update.save()
        return redirect('experience')
    return render(request, 'experience_pages/update_experience.html', context={'experience': experience_to_update})

def experience_delete(request, experience_index):
    experience_to_delete = Experience.objects.get(pk=experience_index)
    if request.method == 'POST':
        experience_to_delete.delete()
        return redirect('experience')
    return render(request, 'experience_pages/delete_experience.html', context={'experience': experience_to_delete})


