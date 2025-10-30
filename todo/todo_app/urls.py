from django.urls import path
from .views import (
    home_view,
    tasks_list_view,
    add_task_view,
    complete_task_view,
    delete_task_view,
    edit_task_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('tasks/list/', tasks_list_view, name='tasks_list'),
    path('tasks/add/', add_task_view, name='add_task'),
    path('tasks/complete/<int:task_id>/', complete_task_view, name='complete_task'),
    path('tasks/delete/<int:task_id>/', delete_task_view, name='delete_task'),
    path('tasks/edit/<int:task_id>/', edit_task_view, name='edit_task'),
]
