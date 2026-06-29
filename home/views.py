from django.shortcuts import render
from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience
from projects.models import Project

def home_view(request):
    bio = Bio.objects.first()
    education_list = Education.objects.all()
    skills_list = Skill.objects.all()
    experience_obj = Experience.objects.first()
    project_list = Project.objects.all()
    
    # We can also group skills by category for nice visual sections in the UI
    categories = {}
    for skill in skills_list:
        categories.setdefault(skill.category, []).append(skill)

    context = {
        'bio': bio,
        'education_list': education_list,
        'skills_list': skills_list,
        'skills_by_category': categories,
        'experience': experience_obj,
        'project_list': project_list,
    }
    return render(request, 'home/index.html', context)
