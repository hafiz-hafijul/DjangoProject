from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.sign_up, name='signin'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('password_change/', views.user_passwordChange, name='password_change'),
]
