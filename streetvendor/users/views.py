from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, LoginForm
# Create your views here.

def signupview(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    
    else:  
        form = UserRegistrationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'signup.html', context)  


def loginview(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("/")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    

def logoutview(request):
    logout(request)
    # Redirect to a success page.
    return redirect("/")