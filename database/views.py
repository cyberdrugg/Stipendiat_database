from django.shortcuts import render, get_object_or_404

from database import models
from .filters import StudentFilter


# Create your views here.
def spisok(request):
    data = models.Student.objects.all()
    myFilter = StudentFilter(request.GET, queryset=data)
    data = myFilter.qs
    context = {'data': data, 'myFilter': myFilter}
    return render(request, 'main_spisok.html', context)


def view_student(request, id):
    data = get_object_or_404(models.Student, id=id)
    return render(request, 'profile.html', {'data': data})


def view_news(request):
    news = models.News.objects.all()
    return render(request, 'news_list.html', {'news': news})


def news(request, id):
    news = get_object_or_404(models.News, id=id)
    return render(request, 'news.html', {'news': news})


def main(request):
    data = models.News.objects.all()
    return render(request, 'main_page.html', {'data': data})


def main_new(request):
    data = models.News.objects.all()
    return render(request, 'main_new.html', {'data': data})

