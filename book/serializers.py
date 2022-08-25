import json
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Author, Books
from django.db import transaction


class BookSeria(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Books
        fields = "__all__"
        read_only_fields = (
            'author',
        )


class AuthorSerial(serializers.ModelSerializer):
    book = BookSeria(many=True)

    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        book_name = validated_data.pop('book')
        author = Author.objects.create(**validated_data)
        for bk in book_name:
            Books.objects.create(**bk, author=author)
        return author

    def update(self, instance, validated_data):
        book_data = validated_data.pop("book")
        instance.author = validated_data.get("author", instance.author)
        instance.save()
        keep_book = []
        for bk in book_data:
            if "id" in bk.keys():
                if Books.objects.filter(id=bk["id"]).exists():
                    c = Books.objects.get(id=bk["id"])
                    c.name = bk.get("name", c.id)
                    c.save()
                else:
                    continue
            else:
                c = Books.objects.create(**bk, author=instance)
                keep_book.append(c.id)

        for bk_data in instance.book:
            print(1, bk_data)
            if bk_data.id not in keep_book:
                bk_data.delete()
        return instance


class AuthorListSerializer(serializers.ModelSerializer):
    book = BookSeria(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
