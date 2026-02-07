from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path('ask_einstein/', views.ask_einstein, name='ask_einstein'),
]

