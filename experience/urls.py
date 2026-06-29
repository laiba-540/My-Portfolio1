from django.urls import path
from . import views

app_name = 'experience'

urlpatterns = [
    path('', views.experience_detail, name='experience_detail'),
]
