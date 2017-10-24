from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=64, null=True)
    description = models.TextField(max_length=255)
    url = models.URLField()
    urlToImage = models.URLField()
    publishedAt = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return 'Title:{}'.format(self.title)
