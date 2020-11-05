from django.urls import path
from . import views

urlpatterns = [
    path('sign/',views.showdata, name= 'home'),
    path('success/',views.thank)
]
