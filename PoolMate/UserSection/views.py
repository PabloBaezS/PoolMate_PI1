from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db import IntegrityError
from .forms import SignUpForm
from django.shortcuts import render, redirect
from .models import Vehicle

def signupAccount(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'signUp.html', {'form': form})
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                try:
                    user = form.save()
                    login(request, user)
                    return redirect('dashboard.html', user)
                except IntegrityError:
                    return render(request, 'signUp.html', {'form': form, 'error': 'Username already taken. Choose a new username.'})
            else:
                return render(request, 'signUp.html', {'form': form, 'error': 'Passwords do not match.'})
        else:
            return render(request, 'dashboard.html', {'form': form})


@login_required
def logoutAccount(request):
    logout(request)
    return redirect('home')

def loginAccount(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Authentication successful, log the user in
            login(request, user)
            return redirect('dashboard.html')  # Replace 'home' with the URL name for the home page
        else:
            # Authentication failed, show an error message
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'dashboard.html')


def index(request):
    return render(request, 'index.html')

def security(request):
    return render(request, 'security.html')

def PoolMate(request):
    return render(request, 'PoolMate.html')

@login_required
def dashboard(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'dashboard.html', context)

@login_required
def passenger_dashboard(request):
    if not request.user.is_passenger:
        return redirect('dashboard')  # Redirect to normal dashboard
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'passenger_dashboard.html', context)

@login_required
def driver_dashboard(request):
    if not request.user.is_driver:
        return redirect('dashboard')  # Redirect to normal dashboard
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'driver_dashboard.html', context)


def driver_vehicle_info(request):
    message = None

    if request.method == 'POST':
        model = request.POST.get('model')
        license_plate = request.POST.get('licensePlate')
        color = request.POST.get('color')
        driver_id = request.POST.get('driverId')
        capacity = request.POST.get('capacity')

        # Save the vehicle information to the database
        vehicle = Vehicle.objects.create(
            model=model,
            licensePlate=license_plate,
            color=color,
            driverId=driver_id,
            capacity=capacity
        )

        # Optionally, you can associate the vehicle with the logged-in driver
        # driver = request.user.driver
        # driver.car = vehicle
        # driver.save()

        message = "Vehicle information saved successfully!"

    return render(request, 'vehicle.html', {'message': message})