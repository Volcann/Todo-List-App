from django.urls import path
from . import views

urlpatterns = [
     path('', views.apioverview, name='api-overview'),
     path('task/', views.todolist, name='task-list'),
     path('task/<str:pk>/', views.taskdetail, name='task-detail'),
     path('task-create/', views.taskcreate, name='task-create'),
     path('task-update/<str:pk>/', views.taskupdate, name='task-update'),
     path('task-del/<str:pk>/', views.taskdelete, name='task-del'),
]