from django.urls import path
from employee import views

urlpatterns = [
    path('post-employee/', views.post_employee),
]
