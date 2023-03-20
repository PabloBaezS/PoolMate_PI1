from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        homeAddress = re

        # Create user object and save to database
        user = User.objects.create_user(username, email, password)
        user.save()

        # Authenticate and login user
        user = authenticate(username=username, password=password)
        login(request, user)

        # Redirect to home page or some other page
        return redirect('home')
    else:
        return render(request, 'registration/register.html')
