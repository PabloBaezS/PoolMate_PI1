from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import UserProfile


def SignUpFunction(request):
    id = 0
    if request.method == 'POST':
        id = id + 1
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        homeAddress = request.POST.get('homeAddress')
        user = User.objects.create_user(name, email, password, phone, homeAddress, id)
        user.save()
        user = authenticate(name=name, password=password)
        login(request, user)
        # Redirect to home page or some other page
        return redirect('map.html')
    else:
        return render(request, 'signUp.html')


def view_user(request, user_id):
    user = User.objects.get(id=user_id)
    context = {'user': user}
    return render(request, 'userInfo.html', {id(1)})
