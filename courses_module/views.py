from django.shortcuts import render
from .models import Course

# Create your views here.


def courses_view(request):
    queryset = Course.objects.all()
    context = {"courses": queryset}
    return render(request, "appPages/courses.html", context)


def course_view(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/course.html', {'obj': course})


def get_certified_view(request):
    return render(request, 'appPages/certificate.html')
