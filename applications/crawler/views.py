import requests
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from rest_framework import generics

from applications.crawler.models import Article
from . import models
from . import serializers

from applications.crawler.utils import PageLinksMixin


# HTML views
# class ArticleList(PageLinksMixin, View):
#     def get(self, request, parent_template=None):
#         return render(
#             request,
#             'crawler/crawler_list.html',
#             {'news_list': models.Article.objects.all(),
#              'parent_template': parent_template})

class ArticleList(PageLinksMixin, View):
    def get(self, request):
        r = requests.get('https://newsapi.org/v1/articles?source=techcrunch&apiKey=af92652e76b745a6bde8dd2fc5739bfd')
        articles = r.json()
        return render(request, 'crawler/crawler_list.html', articles)


class JsonArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.NewsSerializer
