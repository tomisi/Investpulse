from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # This matches the name attribute of your email input
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Email Taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password)  # Using email as username
            user.save()
            return redirect('login')
        
    else:
        return render(request, 'getstarted.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('login')