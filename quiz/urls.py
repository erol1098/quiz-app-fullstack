from django.urls import path,include

from .views import CategoryList, QuizList

urlpatterns = [

    path("", CategoryList.as_view()),
    path("quiz/", QuizList.as_view()),
]
