from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, DetailView
from .models import Publisher

class QuestionView(TemplateView):
    template_name = "base.html"

class PublisherList(ListView):

    template_name = "list.html"
    model = Publisher

    #通常はtemplateに"for hoge in object_list"と記述するが
    # その"object_listの名前を変更している。"
    context_object_name = 'my_favorite_publishers'
    slug_field = "name"

class ListDetail(DetailView):

    model = Publisher
    template_name = "detail.html"



