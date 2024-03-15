from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.about, name='aboutus'),
    path('services/', views.service, name='services'),
    path('prices/', views.price, name='prices'),
]