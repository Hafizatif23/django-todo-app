from django.shortcuts import render, redirect
from .models import Task


def home(request):
    
    if request.method == "POST":
        new_task = request.POST.get('new_task')
        Task.objects.create(title = new_task)
        return redirect('home')

    tasks = Task.objects.all()
    return render(request, "todoapp/home.html", {"tasks": tasks})

def delete_task(request, task_id):

    del_task = Task.objects.get(id=task_id)
    del_task.delete()
    return redirect('home')


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == "POST":
        new_title = request.POST.get('new_title')
        task.title = new_title
        task.save()
        return redirect('home')
    
    return render(request, "todoapp/edit.html", {"task": task})


def done_task(request, task_id):

    task = Task.objects.get(id=task_id)

    task.done = not task.done
    task.save()
    return redirect('home')