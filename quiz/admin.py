from django.contrib import admin

from quiz.models import Category, Option, Question, Quiz

# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)