from django.contrib import admin
from .models import Contact, Questions, QuestionFiles, Subject


admin.site.register(Contact)
admin.site.register(Questions)
admin.site.register(QuestionFiles)
admin.site.register(Subject)