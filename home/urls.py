from django.urls import path 
from . import views
from django.contrib import admin

urlpatterns = [
    path('',views.home, name='home'),
    path('play/<room_code>',views.play, name='play')
]