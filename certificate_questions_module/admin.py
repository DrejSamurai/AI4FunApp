from django.contrib import admin
from .models import CertificateQuestion, CertificateAnswer
# Register your models here.


class CertificateAnswerInline(admin.TabularInline):
    model = CertificateAnswer


class CertificateQuestionAdmin(admin.ModelAdmin):
    inlines = [CertificateAnswerInline]


admin.site.register(CertificateQuestion, CertificateQuestionAdmin)
admin.site.register(CertificateAnswer)