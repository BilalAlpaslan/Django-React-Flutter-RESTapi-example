from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,TaggitSerializer)
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *


class ArticleSerializer(TaggitSerializer,serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','slug','author','name','description','image','created_date']
