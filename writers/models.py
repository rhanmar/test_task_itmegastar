from django.db import models
from django.utils.translation import gettext as _


class Writer(models.Model):
    """
    Модель с информацией о Писателе.
    """
    first_name = models.CharField(
        max_length=64,
        verbose_name=_("Имя писателя")
    )
    last_name = models.CharField(
        max_length=64,
        verbose_name=_("Фамилия писателя")
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Писатель")
        verbose_name_plural = _("Писатели")


class Book(models.Model):
    """
    Модель с информацией о книгах.
    """
    author = models.ForeignKey(
        "writers.Writer",
        verbose_name=_("Автор книги"),
        related_name="books",
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name=_("Название книги"),
        max_length=256,
    )

    def __str__(self):
        return f"{self.author.full_name}: {self.name}"

    class Meta:
        verbose_name = _("Книга")
        verbose_name_plural = _("Книги")
