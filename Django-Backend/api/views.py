from .models import *
from django.contrib.auth.models import User
from django.conf import settings
from django.http.multipartparser import MultiPartParser as DjangoMultiPartParser, MultiPartParserError
from rest_framework.decorators import authentication_classes, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets,filters
from rest_framework import permissions,generics
from .serializer import *



class ActionBasedPermission(permissions.AllowAny):
    # Grant or deny access to a view, based on a mapping in view.action_permissions
    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False


class ArticleViewSet(viewsets.ModelViewSet):
    search_fields = ['description','name']
    filterset_fields = ['author__id',]
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        permissions.IsAuthenticated: ['update', 'partial_update', 'destroy', 'create'],
        permissions.AllowAny: ['list','retrieve']
    }
