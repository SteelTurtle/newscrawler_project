import random

import requests
from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics

from . import serializers
from .models import Article
from .utils import PageLinksMixin


class ArticleList(PageLinksMixin, ListView):
    model = Article
    paginate_by = 5

    def get(self, request):
        random_sources = ['techcrunch',
                          'bild',
                          'the-guardian-uk',
                          'reuters',
                          ]
        base_url = 'https://newsapi.org/v1/articles'
        source = random.choice(random_sources)
        sortBy = 'top'
        apiKey = settings.NEWSAPI_KEY
        r = requests.get(base_url, {
            'source': source,
            'sortBy': sortBy,
            'apiKey': apiKey, }, timeout=10)
        articles = r.json()
        articles_list = articles.get('articles')
        for (i, item) in enumerate(articles_list):
            a = Article()
            a.author = articles_list[i]['author']
            a.title = articles_list[i]['title']
            a.description = articles_list[i]['description']
            a.url = articles_list[i]['url']
            a.urlToImage = articles_list[i]['urlToImage']
            a.publishedAt = articles_list[i]['publishedAt']
            a.save()

        return render(request, 'crawler/crawler_list.html', articles)


class JsonArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.NewsSerializer
