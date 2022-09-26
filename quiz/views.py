from django.shortcuts import render
from rest_framework import generics
from django_filters import DjangoFilterBackend

from .models import Category, Option, Question, Quiz
from .serializers import CategorySerializer,QuizSerializer
# Create your views here.

class CategoryList(generics.ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class QuizList(generics.ListAPIView):
  queryset = Quiz.objects.all()
  serializer_class = QuizSerializer
  filter_backends = [DjangoFilterBackend]  
  filterset_fields = ["category"]