from .views import courses, home
from django.urls import path
urlpatterns = [
    path('courses/', courses, name='courses'),
    path('', home, name='home'),
]