from django.contrib import admin

from database import models

# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.News)