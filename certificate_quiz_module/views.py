from django.shortcuts import render, redirect
from .models import CertificateQuiz
from django.views.generic import ListView
from django.http import JsonResponse
from certificate_questions_module.models import CertificateQuestion,CertificateAnswer
from  certificate_results_module.models import CertificateResult

# Create your views here.


# This is the main quiz page from the navbar
def tests_view(request):
    if request.user.is_authenticated:
        queryset = CertificateQuiz.objects.all()
        context = {"quizes": queryset}
        return render(request, 'appPages/certificate.html', context=context)
    else:
        return redirect('/signin')


def quiz_view(request, pk):
    quiz = CertificateQuiz.objects.get(pk=pk)
    return render(request, 'appPages/certificateTest.html', {'obj': quiz})


def quiz_data_view(request, pk):
    quiz = CertificateQuiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


def save_quiz_view(request, pk):
    # print(request.POST)
    questions = []
    if request.accepts("application/json"):
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = CertificateQuestion.objects.get(text=k)
            questions.append(question)

    print(questions)

    user = request.user
    quiz = CertificateQuiz.objects.get(pk=pk)

    score = 0
    multiplier = 100 / quiz.number_of_questions
    results = []
    correct_answer = None

    for q in questions:
        a_selected = request.POST.get(q.text)

        if a_selected != "":
            question_answers = CertificateAnswer.objects.filter(question=q)
            for a in question_answers:
                if a_selected == a.text:
                    if a.correct:
                        score += 1
                        correct_answer = a.text
                else:
                    if a.correct:
                        correct_answer = a.text
            results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
        else:
            results.append({str(q): 'not answered'})

    score_ = score * multiplier
    CertificateResult.objects.create(quiz=quiz, user=user, score=score_)

    if score_ >= quiz.required_score_to_pass:
        return JsonResponse({'passed': True, 'score': score_, 'results': results})
    else:
        return JsonResponse({'passed': False, 'score': score_, 'results': results})


