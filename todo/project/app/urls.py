from django.urls import path
from . import views

urlpatterns = [
     path('', views.apioverview, name='api-overview'),
     path('task/', views.todolist, name='task-list'),
]