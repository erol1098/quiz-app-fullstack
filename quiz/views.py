from encodings import search_function
from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Category, Option, Question, Quiz
from .serializers import CategorySerializer,QuizSerializer, QuestionSerializer
# Create your views here.

class CategoryList(generics.ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class QuizList(generics.ListAPIView):
  queryset = Quiz.objects.all()
  serializer_class = QuizSerializer
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]  
  filterset_fields = ["category"]
  search_fields = ["title"]

class QuestionView(generics.ListAPIView):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer
