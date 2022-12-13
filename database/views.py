from django.shortcuts import render, get_object_or_404

from database import models


# Create your views here.
def spisok(request):
    data = models.Student.objects.all()
    return render(request, 'main_spisok.html', {'data': data})


def view_student(request, id):
    data = get_object_or_404(models.Student, id=id)
    return render(request, 'profile.html', {'data': data})


from django.shortcuts import render
from django_table_sort.table import TableSort
from database.models import Student


def view(request):
    data = TableSort(request, Student.objects.all())
    return render(request, "main_spisok.html", context={'data': data})


def view_news(request):
    news = models.News.objects.all()
    return render(request, 'news_list.html', {'news': news})


def news(request, id):
    news = get_object_or_404(models.News, id=id)
    return render(request, 'news.html', {'news': news})
