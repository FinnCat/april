from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home_home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Bad login attempt, no such user'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        print('yritetään uloskirjausta')
        auth.logout(request)
        return redirect('home_home')
    else:
        print('jokin ei täsmää:  ' + request.method)
        return redirect('home_home')

def signup(request):
    # the user wants to create account
    if request.method == 'POST':
        if request.POST['password_01'] == request.POST['password_02']:
            try:
                user = User.objects.get(username=request.POST['username'])
                print(user)
                return render(request, 'accounts/signup.html', {'error': 'Username exists already'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],'',request.POST['password_01'])
                print('User created succesfully')
                auth.login(request, user)

                return redirect('home_home')
        else:
            print('password match error')
            return render(request, 'accounts/signup.html', {'error': 'Passwords are not equal'})
    else:
        return render(request, 'accounts/signup.html')

