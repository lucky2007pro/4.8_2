from django.shortcuts import render
from .models import Course
# Create your views here.

def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def home(request):
    courses = Course.objects.all()
    return render(request, 'home_page.html', {'courses': courses})