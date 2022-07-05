from django.contrib import admin
from django.urls import path, include
from .views import view_profile, certificate_pdf_view

urlpatterns = [
    path('view_profile', view_profile, name="view-profile"),
    path('view_certificate', certificate_pdf_view, name="certificate-view"),
]
