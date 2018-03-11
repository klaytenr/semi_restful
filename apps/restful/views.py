from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    context = {
        'full_name' : Users.objects.all()
    }
    return render(request, "restful/index.html", context)

def view(request, id):
    context = {
        'full_name' : Users.objects.filter(id=id)
    }
    return render(request, "restful/view.html", context)

def new(request):
    return render(request, "restful/new.html")

def edit(request, id):
    context = {
        'current' : Users.objects.filter(id=id)
    }
    return render(request, "restful/edit.html", context)

def create(request):
    Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect('/users')

def update(request, id):
    user = Users.objects.get(id=id)
    user.first_name=request.POST['first_name']
    user.last_name=request.POST['last_name']
    user.email=request.POST['email']
    user.save()
    return redirect("/users/" + id)

def delete(request, id):
    user = Users.objects.get(id=id)
    user.delete()
    return redirect("/users")