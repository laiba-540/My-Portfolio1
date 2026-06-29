from django.http import JsonResponse
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    data = []
    for project in projects:
        data.append({
            'title': project.title,
            'description': project.description,
            'image': project.image.url if project.image else None,
            'technologies': project.get_technologies_list(),
            'github_link': project.github_link,
            'live_link': project.live_link
        })
    return JsonResponse(data, safe=False)
