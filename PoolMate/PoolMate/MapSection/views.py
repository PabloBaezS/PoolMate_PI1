from django.shortcuts import render, redirect
from .forms import CreateRideForm

def create_route(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = CreateRideForm(request.POST)
        if form.is_valid():
            route = form.save(commit=False)
            route.user = request.user
            route.save()
            return redirect('map')
    else:
        form = CreateRideForm()

    context = {'form': form}
    return render(request, 'map/create_route.html', context)
