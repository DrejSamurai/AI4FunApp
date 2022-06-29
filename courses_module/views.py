from django.shortcuts import render, redirect
from .models import Course
from quiz_module.models import Quiz
from .forms import CourseForm
# Create your views here.


def add_course(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/add_course')
    context = {'form': form}
    return render(request, 'appPages/addCourse.html', context)


def edit_course(request, pk):
    course = Course.objects.get(pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('/courses')
    context = {'course': course, 'form': form}
    return render(request, 'appPages/editCourse.html', context)


def delete_event(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return redirect('/courses')

def courses_view(request):
    queryset = Course.objects.all()
    context = {"courses": queryset}
    return render(request, "appPages/courses.html", context)


def course_view(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/course.html', {'obj': course})


def get_certified_view(request):
    quiz = Quiz.objects.filter(name="Certificate Quiz").get()
    return render(request, 'appPages/certificate.html', {"quiz": quiz})


def get_certificet_test_view(request):
    return render(request, "appPages/certificateTest.html")