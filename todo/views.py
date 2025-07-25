from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404

from todo.models import TaskDetails


def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')

        tt = TaskDetails(task=task,priority=priority,date=date)
        tt.save()
        return redirect('/')

    tasks = TaskDetails.objects.filter(completed=False).order_by('priority')
    completed_tasks = TaskDetails.objects.filter(completed=True).order_by('date')

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }

    return render(request, 'home.html', context=context)


def update(request, id):
    task = get_object_or_404(TaskDetails, id=id)
    if request.method == 'POST':
        task_name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')

        task.task = task_name
        task.priority = priority
        task.date = date
        task.save()
        return redirect('/')

    return render(request, 'update.html', {'task': task})


def delete(request, id):
    task = get_object_or_404(TaskDetails, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task': task})

def mark_as_done(request, id):
    task = get_object_or_404(TaskDetails, id=id)
    task.completed = True
    task.date = timezone.now()
    task.save()
    return redirect('/')
