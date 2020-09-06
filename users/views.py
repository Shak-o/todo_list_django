from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def registration (request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        if User.objects.filter(username=username):
            return redirect ('/reg/err')
        else:
            user= User.objects.create_user(username=username,password=password1)
            user.save()
        return redirect('/')
    return render(request,'users/registration.html')

def regerr(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        if User.objects.filter(username=username):
            return redirect('/reg/err')
        else:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
        return redirect('/')
    return render(request,'users/regerr.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            return redirect('/error')
    else:
        return render(request,'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def error (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            return redirect('/error')
    else:
        return render(request,'users/login_error.html')