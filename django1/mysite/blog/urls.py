from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.identity),
    path('single/', views.single_page, name='single'),
]
