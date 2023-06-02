from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('create/', views.createTask),
    path('view_tasks/', views.viewTask),
    path('edit/', views.editTask),
    path('delete/', views.deleteTask)
]