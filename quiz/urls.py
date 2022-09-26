from django.urls import path,include

from .views import CategoryList, QuestionView, QuizList

urlpatterns = [

    path("", CategoryList.as_view()),
    path("quiz/", QuizList.as_view()),
    path("questions/", QuestionView.as_view()),
]
