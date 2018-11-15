from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import threading
from .models import *
import time

def index(request):
    return render(request, 'index.html', locals())

def startThreadTask(request):
    task = ThreadTask()
    task.save()
    t = threading.Thread(target=longTask,args=[task.id])
    t.setDaemon(True)
    t.start()
    return JsonResponse({'id':task.id})

def checkThreadTask(request,id):
    task = ThreadTask.objects.get(pk=id)
    return JsonResponse({'is_done':task.is_done})

def longTask(id):
    print("Received task",id)
    time.sleep(3)
    task = ThreadTask.objects.get(pk=id)
    task.is_done = True
    task.save()
    print("Finishing task",id)

