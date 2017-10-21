from django.views.generic import ListView

from rest_framework.views import APIView
from rest_framework.response import Response

from applications.crawler.utils import PageLinksMixin


# HTML views
class ArticleList(PageLinksMixin, ListView):
    template_name = 'crawler/crawler_article_list.html'
