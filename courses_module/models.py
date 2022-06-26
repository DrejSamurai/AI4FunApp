from django.db import models

# Create your models here.

DIFF_CHOICES = (
    ('novice', 'bnovice'),
    ('beginner', 'beginner'),
    ('proficient', 'proficient'),
    ('master', 'master'),
)


class Code(models.Model):
    code = models.TextField()

    def __str__(self):
        return f"{self.code}"


class Course(models.Model):
    name = models.CharField(max_length=60)
    topic = models.CharField(max_length=60)
    difficulty = models.CharField(max_length=12, choices=DIFF_CHOICES)
    text = models.TextField()
    code = models.ForeignKey(Code, on_delete=models.CASCADE)



