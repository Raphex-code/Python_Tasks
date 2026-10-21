from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Task
from .forms import TaskForm


def task_list_view(request):
    tasks = Task.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form = TaskForm()

    return render(request, 'task_app/task_list.html', {
        'tasks': tasks,
        'form': form,
    })


def update_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form = TaskForm(instance=task)

    return render(request, 'task_app/update_task.html', {'form': form, 'task': task})


def delete_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')


def toggle_complete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    if task.completed:
        task.completed_at = timezone.now()
    else:
        task.completed_at = None
        
    task.save()
    return redirect('task_list')
