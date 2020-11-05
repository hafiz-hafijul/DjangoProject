from django.urls import path
from main import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('testimonials/', views.testimonials, name='testimonials'),
]
