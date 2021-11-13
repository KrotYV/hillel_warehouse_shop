import uuid

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
    reservation = models.BooleanField(default=False)

    class Meta:
        ordering = ('title', 'genre',)

    def __str__(self):
        return self.title


class PublishingOffice(models.Model):
    name = models.CharField(max_length=200)
    pub_year = models.IntegerField(default=2000)

    def __str__(self):
        return self.name


STATUS = (
    ('A', 'available'),
    ('R', 'reserved'),
    ('S', 'sold out')
)


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    publish = models.ForeignKey(PublishingOffice, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS)
    receiving_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.id} ({self.book})'
