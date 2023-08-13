from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskForm

def home(request):
    return render(request, 'home.html')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def show_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=False)
    return render(request, 'show_tasks.html', {'tasks': tasks})

def delete_task(request, taskTitle):
    task = get_object_or_404(TaskModel, taskTitle=taskTitle)
    task.delete()
    return redirect('show_tasks')

def edit_task(request, taskTitle):
    task = get_object_or_404(TaskModel, taskTitle=taskTitle)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

def complete_task(request, taskTitle):
    task = get_object_or_404(TaskModel, taskTitle=taskTitle)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')
def completed_tasks(request):
    completed_tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})

