from django.core.management.base import BaseCommand
from writers.models import Book, Writer


class Command(BaseCommand):
    help = 'Заполнение БД тестовыми данными'

    def handle(self, *args, **kwargs):
        w1 = Writer.objects.create(first_name="Леонид", last_name="Андреев")
        w2 = Writer.objects.create(first_name="Лев", last_name="Толстой")

        Book.objects.create(name="Кусака", author=w1)
        Book.objects.create(name="Иуда Искариот", author=w1)

        Book.objects.create(name="Война и мир", author=w2)
        Book.objects.create(name="Анна Каренина", author=w2)

        print("Окончание заполнения БД тестовыми данными")
