import random

import requests
from django.conf import settings
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from . import serializers
from .models import Article


class JsonArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.NewsSerializer
    pagination_class = PageNumberPagination


class ArticleList(View):
    page_kwarg = 'page'
    paginate_by = 5
    template_name = 'crawler/crawler_list.html'

    def get(self, request):

        # REST client: request and save the newsfeed every time
        # the browser trigger a GET request
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
            a.title = articles_list[i]['title']
            # Do not save again in the DB the same article
            if not Article.objects.filter(title__iexact=a.title):
                a.author = articles_list[i]['author']
                a.description = articles_list[i]['description']
                a.url = articles_list[i]['url']
                a.urlToImage = articles_list[i]['urlToImage']
                a.publishedAt = articles_list[i]['publishedAt']
                a.save()

        # Paginator configuration:
        # Get the FULL list of articles to be displayed from the DB
        articles_from_db = Article.objects.all()

        paginator = Paginator(
            articles_from_db, self.paginate_by)
        page_number = request.GET.get(
            self.page_kwarg)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.next_page_number())
        else:
            next_url = None

        context = {
            'is_paginated':
                page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'articles_list': page,
        }
        return render(
            request, self.template_name, context)
