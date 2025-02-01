from django.urls import path
from . import views

urlpatterns = [
    path('e1/', views.Course, name='Course'),
    path('e1/', views.Student, name='Student'),
]