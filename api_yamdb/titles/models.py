from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models


class Genre(models.Model):
    """Модель жанра."""
    name = models.CharField('Жанр', max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.slug


class Category(models.Model):
    """Модель категории."""
    name = models.CharField('Категория', max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.slug


class Title(models.Model):
    """Модель произведения."""
    name = models.CharField('Название', max_length=100)
    year = models.IntegerField(
        'Год',
        validators=[MaxValueValidator(int(datetime.now().year))]
    )
    rating = models.IntegerField(null=True, default=None)
    description = models.TextField('Описание', null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория'
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        verbose_name='Жанр'
    )

    class Meta:
        ordering = ('-year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
