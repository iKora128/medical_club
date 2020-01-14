from django.contrib import admin
from django.urls import path, include
from .views import QuestionView

urlpatterns = [
  path('/', QuestionView.as_view()),
]
