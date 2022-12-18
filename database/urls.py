from django.urls import path
from . import views

urlpatterns = [
    path("main_spisok22_all/", views.spisok, name="main_spisok"),
    path("main_spisok_22/", views.spisok22, name="main_spisok"),
    path("main_spisok_21/", views.spisok21, name="main_spisok"),
    path("main_spisok_20/", views.spisok20, name="main_spisok"),
    path("main_spisok_19/", views.spisok19, name="main_spisok"),
    path("profile/<int:id>/", views.view_student22, name="profile"),
    path("profile/<int:id>/", views.view_student21, name="profile"),
    path("profile/<int:id>/", views.view_student20, name="profile"),
    path("profile/<int:id>/", views.view_student19, name="profile"),
    path("news_list/", views.view_news, name="news"),
    path("news/<int:id>/", views.news, name="news"),
    path("main/", views.main, name="main"),
]
