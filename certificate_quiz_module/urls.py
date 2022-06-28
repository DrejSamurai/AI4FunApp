from django.urls import path
from .views import tests_view, quiz_view, quiz_data_view, save_quiz_view

app_name = 'certificate_quiz_module'

urlpatterns = [
    path('certificate_test', tests_view, name='tests_view'),
    path('certificate_test/<pk>/', quiz_view, name='quiz-view'),
    path('certificate_test/<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('certificate_test/<pk>/save/', save_quiz_view, name='save-view'),
]