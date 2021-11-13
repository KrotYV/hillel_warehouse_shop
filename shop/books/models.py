from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, verbose_name='authors')
    description = models.TextField(max_length=1000, help_text='Description of the book')
    genre = models.ManyToManyField(Genre, verbose_name='genre')
    rating = models.FloatField(default=0)
    reservation = models.BooleanField(default=True)

    class Meta:
        ordering = ('title', 'genre',)

    def __str__(self):
        return self.title

