from django.http import JsonResponse
from .models import Skill

def skills_list(request):
    skills = Skill.objects.all()
    data = []
    for skill in skills:
        data.append({
            'name': skill.name,
            'proficiency': skill.proficiency,
            'category': skill.category
        })
    return JsonResponse(data, safe=False)
