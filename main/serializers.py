from rest_framework import serializers
from .models import *

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ArticleSerializers(serializers.ModelSerializer):
    tags = TagSerializers()
    class Meta:
        model = Article
        fields = '__all__'
        lookup_field = 'slug'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        tags = Tag.objects.create(**tags_data)
        res = Article.objects.create(tags=tags, **validated_data)
        return res