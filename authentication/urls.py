from django.urls import path, include
from . import views
from .views import RegisterView, LoginView, UserView, LogoutView


urlpatterns = [
    path('', include('djoser.urls')),   
    path('', include('djoser.urls.jwt')),    
]