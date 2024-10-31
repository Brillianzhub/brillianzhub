from taggit.models import Tag
# from django.db.models import Count

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer, UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.published().order_by('-publish')
    serializer_class = BlogSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # post = serializer.data

        # Additional data
        related_posts = Blog.objects.filter(
            tags__in=instance.tags.all()).exclude(id=instance.id)
        related_posts_serializer = BlogSerializer(
            related_posts, many=True, context={'request': request})

        categories = Category.objects.all()
        categories_serializer = CategorySerializer(
            categories, many=True, context={'request': request})

        seo_title = f'{instance.title}'
        seo_description = f'{instance.description}'
        og_title = f'{instance.title}'
        og_description = f'{instance.description}'

        data = {
            'post': serializer.data,
            'related_posts': related_posts_serializer.data,
            'categories': categories_serializer.data,
            'seo_title': seo_title,
            'seo_description': seo_description,
            'og_title': og_title,
            'og_description': og_description
        }

        return Response(data)
