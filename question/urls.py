from django.contrib import admin
from django.urls import path, include
from .views import QuestionView, PublisherList, ListDetail

urlpatterns = [
  path("", QuestionView.as_view(), name="top"),
  path("list/", PublisherList.as_view(), name="list"),
  path("list/detail/<uuid:pk>", ListDetail.as_view(), name="detail"),
]
