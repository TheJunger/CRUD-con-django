from django.shortcuts import render,redirect
from django.urls import path
from .createTask import CreateNewTask
from django.middleware.csrf import get_token
from django.http import JsonResponse
from .models import Task
import json
# Create your views here.

def createTask(request):
    if request.method == 'GET':
        print('get')
        csrf_token = get_token(request)
        return JsonResponse({'token':csrf_token})
        #return render(request, 'index.html')
    else:
        print('post')
        data = json.loads(request.body.decode())
        print(data)
        print(data.get('title'))
        print(data.get('description'))
        Task.objects.create(name=data.get('title'),description=data.get('description'))
        return redirect('/view_tasks')
    
def viewTask(request):
        task = Task.objects.all()
        return render(request, 'viewtasks.html',{
            'task': task
    })
        
def editTask(request):
        if request.method == 'GET':
            print('get')
            csrf_token = get_token(request)
            return JsonResponse({'token':csrf_token})
        else:
            print('post')
            data = json.loads(request.body.decode())
            print(data)
            print(data.get('id'))
            tarea = Task.objects.get(id=data.get('id'))
            print(tarea)
            tarea.name = data.get('title')
            tarea.description = data.get('description')
            tarea.save()
            return redirect('/view_tasks')
def deleteTask(request):
        if request.method == 'GET':
            print('get')
            csrf_token = get_token(request)
            return JsonResponse({'token':csrf_token})
        else:
            print('post -------------------')
            data = json.loads(request.body.decode())
            print(data)
            print(data.get('id'))
            tarea = Task.objects.get(id=data.get('id'))
            print(tarea)
            tarea.delete()
            return redirect('/view_tasks')