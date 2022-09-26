from django.contrib import admin
import nested_admin

from quiz.models import Category, Option, Question, Quiz

class OptionAdmin(nested_admin.NestedTabularInline):
  model = Option

class QuestionAdmin(nested_admin.NestedTabularInline):
  model = Question
  inlines = [OptionAdmin]

class QuizAdmin(nested_admin.NestedModelAdmin):
  model =Quiz
  inlines = [QuestionAdmin]




# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Option)