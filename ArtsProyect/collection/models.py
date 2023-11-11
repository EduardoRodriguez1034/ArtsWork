from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Artist(models.Model):
    slug = models.SlugField(max_length=80, unique=True)
    name = models.CharField(max_length=80)
    born_date = models.CharField(max_length=40)


class Genre(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Style(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Period(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Artwork(models.Model):
    author = models.ForeignKey(Artist, on_delete=models.RESTRICT)
    path = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=40, null=True)
    style = models.ForeignKey(Style, null=True, on_delete=models.RESTRICT)
    period = models.ForeignKey(Period, null=True, on_delete=models.RESTRICT)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.RESTRICT)
    image_url = models.URLField()
# Create your models here.
