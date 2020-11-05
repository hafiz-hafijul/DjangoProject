from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name= 'home'),
    path('show/<my_id>/', views.func, name= 'show'),
]