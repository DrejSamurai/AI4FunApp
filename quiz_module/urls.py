from django.urls import path
from .views import tests_view, quiz_view

app_name = 'quiz_module'

urlpatterns = [
    path('tests', tests_view, name='tests_view'),
    path('tests/<pk>', quiz_view, name='quiz-view'),
]