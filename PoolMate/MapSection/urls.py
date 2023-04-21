from django.urls import path
from . import views

urlpatterns = [
    path('create_route/', views.create_route, name='create_route'),
]
