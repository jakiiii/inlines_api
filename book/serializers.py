from rest_framework import serializers

from book.models import Author, Books


class BookSeria(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"
        read_only_fields = (
            'author',
        )


class AuthorSerial(serializers.ModelSerializer):
    pass


class AuthorListSerializer(serializers.ModelSerializer):
    book = BookSeria(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
