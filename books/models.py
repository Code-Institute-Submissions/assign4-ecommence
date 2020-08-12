from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Book(models.Model):
    title = models.CharField(blank=False, max_length=255, validators=[
                             MinLengthValidator(3)])
    published = models.DateField(blank=False)
    ISBN = models.CharField(blank=False, max_length=255)
    length = models.IntegerField(blank=False)
    authors = models.ManyToManyField('author')
    quotes = models.TextField(blank=False)
    desc = models.TextField(blank=False)
    cost = models.DecimalField(max_digits=10, decimal_places=3, blank=False)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=80)
    last_name = models.CharField(blank=False, max_length=80)
    biography=models.TextField(blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

