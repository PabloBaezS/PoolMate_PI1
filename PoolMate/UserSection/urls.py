from django.urls import path
from . import views

urlpatterns = [
 path('signupaccount/', views.signupAccount, name='signUp'),
 path('logout/', views.logoutAccount, name='logout'),
 path('login/', views.loginAccount, name='login'),
]