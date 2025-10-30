from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home_view(request):
    return render(request, 'home.html')

def tasks_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'tasks_list.html', {'tasks': tasks})

def add_task_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('tasks_list')
    return render(request, 'add_task.html')

def edit_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task.title = title
            task.save()
        return redirect('tasks_list')
    return render(request, 'edit_task.html', {'task': task})

def complete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('tasks_list')

def delete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks_list')
