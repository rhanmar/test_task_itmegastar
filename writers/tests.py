from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from .models import Writer, Book


class PointTest(TestCase):

    def setUp(self) -> None:
        self.w1 = Writer.objects.create(first_name="Леонид", last_name="Андреев")
        self.w2 = Writer.objects.create(first_name="Лев", last_name="Толстой")

        self.b1 = Book.objects.create(name="Кусака", author=self.w1)
        self.b2 = Book.objects.create(name="Иуда Искариот", author=self.w1)

        Book.objects.create(name="Война и мир", author=self.w2)
        Book.objects.create(name="Анна Каренина", author=self.w2)

    def test_writers_detail(self):
        url = reverse('writers-detail', args=[self.w1.pk])

        with self.assertNumQueries(2):
            response = self.client.get(url)
        res_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json["books"]), 2)
        self.assertEqual(res_json["books"][0]["id"], self.b1.pk)
        self.assertEqual(res_json["books"][1]["id"], self.b2.pk)

    def test_writers_list(self):
        url = reverse('writers-list')

        with self.assertNumQueries(2):
            response = self.client.get(url)
        res_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), 2)
