from django.db import models
from django.urls import reverse


class Article(models.Model):
    slug = models.SlugField(max_length=64, unique=True)
    source_name = models.CharField(max_length=64, blank=True)
    author = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=64, null=True)
    description = models.TextField(max_length=255)
    url = models.URLField(unique=True)
    image_link = models.URLField(unique=True)
    published_at = models.DateField()

    class Meta:
        get_latest_by = 'published_at'
        ordering = ['-published_at']

    def get_absolute_url(self):
        return reverse('crawler_article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return 'Title:{},published at:{}'.format(self.title, self.published_at)
