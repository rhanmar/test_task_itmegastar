from django.contrib import admin
from .models import Book, Writer


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Book."""
    list_display = ("author", "name")


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Writer."""
    list_display = ("first_name", "last_name")
