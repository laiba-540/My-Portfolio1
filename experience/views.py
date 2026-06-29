from django.http import JsonResponse
from .models import Experience

def experience_detail(request):
    records = Experience.objects.all()
    data = []
    for record in records:
        data.append({
            'title': record.title,
            'description': record.description
        })
    return JsonResponse(data, safe=False)
