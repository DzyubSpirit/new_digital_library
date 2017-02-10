from django.db import models


class Author(models.Model):
    class Meta:
        db_table = 'Author'
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        db_table = 'Book'
    title = models.CharField(max_length=50, unique=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

