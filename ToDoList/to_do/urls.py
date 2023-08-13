from django.urls import path
from .views import home, add_task, show_tasks, edit_task, delete_task, complete_task, completed_tasks

urlpatterns = [
    path('', home, name='home'),
    path('add_task/', add_task, name='add_task'),
    path('show_tasks/', show_tasks, name='show_tasks'),
    path('edit_task/<str:taskTitle>/', edit_task, name='edit_task'),
    path('delete_task/<str:taskTitle>/', delete_task, name='delete_task'),
    path('complete_task/<str:taskTitle>/', complete_task, name='complete_task'),
    path('completed_tasks/', completed_tasks, name='completed_tasks'),
]
