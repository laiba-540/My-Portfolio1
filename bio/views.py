from django.http import JsonResponse
from .models import Bio

def bio_detail(request):
    bio = Bio.objects.first()
    if bio:
        data = {
            'name': bio.name,
            'title': bio.title,
            'summary': bio.summary,
            'email': bio.email,
            'linkedin': bio.linkedin,
            'typing_roles': bio.get_typing_roles_list(),
            'profile_picture': bio.profile_picture.url if bio.profile_picture else None,
            'cv': bio.cv.url if bio.cv else None
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'No bio information available'}, status=404)
