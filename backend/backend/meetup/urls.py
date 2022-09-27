# meetup/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('groups/', views.ListGroups.as_view()),
    path('groups/<str:urlname>/', views.RetrieveGroup.as_view()),
    path('send/', views.Send.as_view()),
]