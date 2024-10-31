from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BlogViewSet, CategoryViewSet, UserViewSet

router = DefaultRouter()
router.register(r'', BlogViewSet, basename='blog')
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
