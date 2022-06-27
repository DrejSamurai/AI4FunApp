from django.urls import path
from .views import tests_view, quiz_view, quiz_data_view, save_quiz_view

app_name = 'quiz_module'

urlpatterns = [
    path('tests', tests_view, name='tests_view'),
    path('tests/<pk>/', quiz_view, name='quiz-view'),
    path('tests/<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('tests/<pk>/save/', save_quiz_view, name='save-view'),
]