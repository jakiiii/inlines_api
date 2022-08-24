from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book.views import AuthorViewSet


author_bok_router = DefaultRouter()


author_bok_router.register('author', AuthorViewSet, basename='author-api'),


urlpatterns = [
    path('', include(author_bok_router.urls))
]
