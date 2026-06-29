from django.http import JsonResponse
from .models import Education

def education_list(request):
    records = Education.objects.all()
    data = []
    for record in records:
        data.append({
            'institution': record.institution,
            'degree': record.degree,
            'status': record.status,
            'start_year': record.start_year,
            'end_year': record.end_year,
            'description': record.description
        })
    return JsonResponse(data, safe=False)
