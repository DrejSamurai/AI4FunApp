from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('courses', views.courses_view, name="courses"),
]
