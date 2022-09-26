from unicodedata import category
from django.db import models

# Create your models here.
class AbstractClass(models.Model):
  class Meta:
    abstract = True


class Category(models.Model):
  name = models.CharField(max_length=255, verbose_name="Category Name")

  class Meta:
    verbose_name_plural = "Categories"
  
  def __str__(self):
    return self.name

  def quiz_count(self):
    return self.quiz_category.count()


class Quiz(models.Model):
  title = models.CharField(max_length=255, verbose_name="Quiz Title")
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="quiz_category")

  class Meta:
    verbose_name_plural = "Quizzes"

  def __str__(self):
    return self.title
  
  def question_count(self):
    return self.quiz_question.count()


class Question(models.Model):

  SCALE =(
    ("B", "beginner"),
    ("I", "intermediete"),
    ("A", "advanced"),
  )

  title = models.TextField()
  quiz = models.ForeignKey(Quiz,related_name="quiz_question", on_delete=models.CASCADE)
  difficulty = models.CharField(max_length=1, choices=SCALE)

  def __str__(self):
    return self.title


class Option(models.Model):
  option_text = models.CharField(max_length=255)
  question = models.ForeignKey(Question,related_name="question_options", on_delete=models.CASCADE)
  is_right = models.BooleanField(default=False)

  def __str__(self):
    return self.option_text