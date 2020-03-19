from django.urls import path
from app import views

urlpatterns = [
    path('hello-world', views.hello_world),
    path('hello', views.hello),
    path('calculator', views.calculator)
]
