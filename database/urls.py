from django.urls import path
from . import views
urlpatterns = [
    path('main_spisok/', views.spisok, name='main_spisok'),
    path('profile/<int:id>/', views.view_student, name='profile'),
    path('news_list/', views.view_news, name='news'),
    path('news/<int:id>/', views.news, name='news')
]