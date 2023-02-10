from django.shortcuts import render, redirect
from django.contrib.auth.models import User as database
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        mydata = authenticate(request, username=username, password=password)
        if mydata is not None:
            login(request, mydata)
            return redirect('homepage')
        else:
            return render(request, 'main/error.html')
    return render(request, 'main/signin.html')

def signup(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!=pass2:
            return render(request, 'main/error.html')
        else:
            myData = database.objects.create_user(username, email, pass1)
            myData.save()
            return redirect('signin')
    return render(request, 'main/signup.html')

@login_required(login_url='signin')
def homepage(request):
    return render(request, 'main/homepage.html')

def logoutpage(request):
    logout(request)
    return redirect('signup')