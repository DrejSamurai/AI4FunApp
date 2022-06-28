from django.db import models
from certificate_quiz_module.models import CertificateQuiz
from django.contrib.auth.models import User

# Create your models here.


class CertificateResult(models.Model):
    quiz = models.ForeignKey(CertificateQuiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)

