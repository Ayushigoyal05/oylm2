from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ListTodo

def todo(request):
    if(request.method=='POST'):
        item=request.POST['todo']
        item_context=ListTodo(todo=item)
        item_context.save()
    all=ListTodo.objects.all()
    return render(request,'todoapp.html',{'all':all})


def delcomp(request):
    p=ListTodo.objects.filter(completed__exact=True).delete()
    return redirect('todo')

def delall(request):
    li=ListTodo.objects.all().delete()
    return redirect('todo')

def complete(request,todo_id):
    todoo=ListTodo.objects.get(pk=todo_id)
    todoo.completed=True
    todoo.save()
    return redirect('todo')









