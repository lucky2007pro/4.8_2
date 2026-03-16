from django.shortcuts import render
from .models import Users
# Create your views here.

def users(request):
    users = Users.objects.all()
    return render(request, 'users.html', {'users': users})