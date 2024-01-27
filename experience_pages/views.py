from django.shortcuts import render,redirect
from .models import Experience
from django.views.generic import ListView
from experience_pages.models import Experience


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



