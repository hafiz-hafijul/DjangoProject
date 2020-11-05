from django.urls import path
from gs import views

urlpatterns = [
    path('',views.home,name='home'),
    path('password/', views.password, name='password')
]
