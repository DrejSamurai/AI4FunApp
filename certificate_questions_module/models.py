from django.db import models
from certificate_quiz_module.models import CertificateQuiz
# Create your models here.


class CertificateQuestion(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(CertificateQuiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.certificateanswer_set.all()


class CertificateAnswer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(CertificateQuestion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question}, answer: {self.text}, correct:{self.correct}"
