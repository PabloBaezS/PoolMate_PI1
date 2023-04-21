from django.shortcuts import render
from .forms import UserCreateForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def signupAccount(request):
    if request.method == 'GET':
        return render(request, 'signUp.html',
            {'form':UserCreateForm})
    else:
        if request.POST['Password1'] == request.POST['Password2']:
            try:
                user = User.objects.create_user(request.POST['Username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signUp.html',
                {'form':UserCreateForm,
                'error':'Username already taken. Choose new username.'})
        else:
            return render(request, 'signUp.html',
            {'form':UserCreateForm, 'error':'Passwords do not match'})

@login_required
def logoutAccount(request):
    logout(request)
    return redirect('home')

def loginAccount(request):
    if request.method == 'GET':
        return render(request, 'login.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['Username'],password=request.POST['Password'])
    if user is None:
        return render(request,'login.html',{'form': AuthenticationForm(),'error': 'Username and Password do not match'})
    else:
        login(request,user)
    return redirect('home')