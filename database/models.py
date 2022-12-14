from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


# Create your models here.

class Student(models.Model):
    GROUPS = (
        ('AIN-1-22', 'AIN-1-22'),
        ('AIN-2-22', 'AIN-2-22'),
        ('MIN-1-22', 'MIN-1-22'),
        ('WIN-1-22', 'WIN-1-22'),
        ('AIN-1-21', 'AIN-1-21'),
        ('AIN-2-21', 'AIN-2-21'),
        ('MIN-1-21', 'MIN-1-21'),
        ('WIN-1-21', 'WIN-1-21'),
        ('AIN-1-20', 'AIN-1-20'),
        ('MIN-1-20', 'MIN-1-20'),
        ('WIN-1-20', 'WIN-1-20'),
        ('AIN-1-19', 'AIN-1-19'),

    )

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    group = models.CharField(choices=GROUPS, max_length=100, null=True)


class News(models.Model):
    title = models.CharField(max_length=150)
    short = models.CharField(max_length=400)
    content = models.TextField()
    image = models.ImageField(upload_to='')
