from django.urls import path
from .views import course_view, courses_view, delete_event, edit_course, add_course

app_name = 'courses_module'

urlpatterns = [
    path('courses', courses_view, name='courses_view'),
    path('courses/<pk>', course_view, name='course_view'),
    path('delete_event/<pk>', delete_event, name='delete-event'),
    path('edit_event/<pk>', edit_course, name='edit-course'),
    path('add_course', add_course, name='add-course')
]
