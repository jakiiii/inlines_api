from rest_framework.viewsets import ModelViewSet

from book.models import Author
from book.serializers import AuthorSerial, AuthorListSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            return AuthorSerial
        return AuthorListSerializer
