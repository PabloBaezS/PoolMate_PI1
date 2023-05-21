from django.urls import path
from . import views
from .views import driver_view, save_route

urlpatterns = [
    path('driver-view/', driver_view, name='driver_view'),
    path('save-route/', save_route, name='save_route'),
]
