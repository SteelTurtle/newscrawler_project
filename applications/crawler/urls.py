from django.conf.urls import url

from applications.crawler.views import ArticleList

urlpatterns = [
    url(r'^$', ArticleList.as_view(), name="crawler_article_list"),
]
