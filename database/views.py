from django.shortcuts import render, get_object_or_404

import database
from database.models import models
from .filters import *


def spisok22(request):
    data = database.models.Students_22.objects.order_by("-average")
    myFilter = StudentFilter22(request.GET, queryset=data)
    data = myFilter.qs
    context = {"data": data, "myFilter": myFilter}
    return render(request, "main_spisok_22.html", context)


def spisok(request):
    data = database.models.Students_22.objects.order_by("-average")
    myFilter = StudentFilter22(request.GET, queryset=data)
    data = myFilter.qs
    context = {"data": data, "myFilter": myFilter}
    return render(request, "main_spisok22_all.html", context)


def spisok21(request):
    data = database.models.Students_21.objects.order_by("-average")
    myFilter = StudentFilter21(request.GET, queryset=data)
    data = myFilter.qs
    context = {"data": data, "myFilter": myFilter}
    return render(request, "main_spisok_21.html", context)


def spisok20(request):
    data = database.models.Students_20.objects.order_by("-average")
    myFilter = StudentFilter20(request.GET, queryset=data)
    data = myFilter.qs
    context = {"data": data, "myFilter": myFilter}
    return render(request, "main_spisok_20.html", context)


def spisok19(request):
    data = database.models.Students_19.objects.order_by("-average")
    myFilter = StudentFilter19(request.GET, queryset=data)
    data = myFilter.qs
    context = {"data": data, "myFilter": myFilter}
    return render(request, "main_spisok_19.html", context)


def view_student22(request, id):
    data = get_object_or_404(database.models.Students_22, id=id)
    context = {"data": data}
    return render(request, "profile.html", context)


def view_student21(request, id):
    data = get_object_or_404(database.models.Students_21, id=id)
    context = {"data": data}
    return render(request, "profile.html", context)


def view_student20(request, id):
    data = get_object_or_404(database.models.Students_20, id=id)
    context = {"data": data}
    return render(request, "profile.html", context)


def view_student19(request, id):
    data = get_object_or_404(database.models.Students_19, id=id)
    context = {"data": data}
    return render(request, "profile.html", context)


def view_news(request):
    news = database.models.News.objects.all()
    return render(request, "news_list.html", {"news": news})


def news(request, id):
    news = get_object_or_404(database.models.News, id=id)
    return render(request, "news.html", {"news": news})


def main(request):
    data = database.models.Main_new.objects.all()
    return render(request, "main_page.html", {"data": data})
