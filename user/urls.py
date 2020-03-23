from django.urls import path
from user import views


urlpatterns = [
    path('signup/', views.create_user),
    path('profile/', views.profile)
]