from django.conf.urls import url

from applications.crawler.views import ArticleList, JsonArticleList

urlpatterns = [
    url(r'^$', ArticleList.as_view(), name='crawler_article_list'),
    url(r'^/api/v1$', JsonArticleList.as_view(), name='crawler_article_jsonlist'),
]
