from django.urls import path
from .views import course_view, courses_view

app_name = 'courses_module'

urlpatterns = [
    path('courses', courses_view, name='courses_view'),
    path('courses/<pk>', course_view, name='course_view'),
]