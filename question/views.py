from django.shortcuts import render
from django.views.generic import TemplateView

class QuestionView(TemplateView):
    template_name = "about.html"
