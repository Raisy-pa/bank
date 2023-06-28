from django.shortcuts import render

# Create your views here.
# banking/views.py

from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        # Process login form data
        return redirect('profile')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        # Process register form data
        return redirect('login')
    return render(request, 'register.html')

def profile(request):
    return render(request, 'profile.html')

def form(request):
    if request.method == 'POST':
        # Process form data
        return redirect('profile')
    return render(request, 'form.html')

def logout(request):
    # Perform logout action
    return redirect('home')
