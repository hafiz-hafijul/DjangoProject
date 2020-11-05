from django.urls import path
from . import views

urlpatterns = [
    path('/',views.home,),
    path('about/',views.about, name='about'),
    path('course/',views.course, name='course'),
    path('contact/',views.contact, name='contact'),
]
