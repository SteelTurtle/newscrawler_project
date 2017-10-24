from rest_framework import serializers

from applications.crawler.models import Article


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
