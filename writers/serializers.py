from rest_framework import serializers
from .models import Writer, Book


class BookSerialzier(serializers.ModelSerializer):
    """Сериалайзер для модели Book."""

    class Meta:
        model = Book
        fields = ("id", "name")


class WriterSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Writer."""

    books = BookSerialzier(many=True, read_only=True)

    class Meta:
        model = Writer
        fields = ("id", "first_name", "last_name", "books")
