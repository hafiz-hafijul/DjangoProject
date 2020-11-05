from django.urls import path
from . import views

urlpatterns = [
    path('sign/', views.showdataform),
    path('success/', views.thank),
]
