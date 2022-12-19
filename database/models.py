from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


# Create your models here.


class Students_22(models.Model):

    GROUPS = (
        ("AIN-1-22", "AIN-1-22"),
        ("AIN-2-22", "AIN-2-22"),
        ("MIN-1-22", "MIN-1-22"),
        ("WIN-1-22", "WIN-1-22"),
    )

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")
    group = models.CharField(choices=GROUPS, max_length=500, null=True)
    phone = models.CharField(max_length=500, null=True)
    email = models.CharField(max_length=500, null=True)
    average = models.FloatField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Students_21(models.Model):
    GROUPS = (
        ("AIN-1-21", "AIN-1-21"),
        ("AIN-2-21", "AIN-2-21"),
        ("MIN-1-21", "MIN-1-21"),
        ("WIN-1-21", "WIN-1-21"),
    )

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")
    group = models.CharField(choices=GROUPS, max_length=500, null=True)
    phone = models.CharField(max_length=500, null=True)
    email = models.CharField(max_length=500, null=True)
    average = models.FloatField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Students_20(models.Model):
    GROUPS = (
        ("AIN-1-20", "AIN-1-20"),
        ("MIN-1-20", "MIN-1-20"),
        ("WIN-1-20", "WIN-1-20"),
    )

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")
    group = models.CharField(choices=GROUPS, max_length=500, null=True)
    phone = models.CharField(max_length=500, null=True)
    email = models.CharField(max_length=500, null=True)
    average = models.FloatField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Students_19(models.Model):
    GROUPS = (("AIN-1-19", "AIN-1-19"),)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")
    group = models.CharField(choices=GROUPS, max_length=500, null=True)
    phone = models.CharField(max_length=500, null=True)
    email = models.CharField(max_length=500, null=True)
    average = models.FloatField(max_length=100, null=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=150)
    short = models.CharField(max_length=400)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.title


class Main_new(models.Model):
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=500, null=True)
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.title
