from rest_framework import serializers

from applications.crawler.models import Article
from . import models


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
