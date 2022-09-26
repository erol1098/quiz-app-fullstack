from dataclasses import fields
from unicodedata import category
from rest_framework import serializers
from quiz.models import Category, Option, Question, Quiz

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ("id","name","quiz_count")


class QuizSerializer(serializers.ModelSerializer):
  category = serializers.StringRelatedField()
  class Meta:
    model = Quiz
    fields = ("id", "title", "category", "question_count")

class OptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Option
    fields = ("id", "option_text", "is_right")

class QuestionSerializer(serializers.ModelSerializer):
  question_options = OptionSerializer(many=True)

  class Meta:
    model = Question
    fields = ("id", "title", "difficulty", "options")
