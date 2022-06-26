from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
# Create your views here.


#This is the main quiz page from the navbar
def tests_view(request):
    queryset = Quiz.objects.all()
    context ={"quizes": queryset}
    return render(request, 'appPages/tests.html', context=context)


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html', {'obj': quiz})
