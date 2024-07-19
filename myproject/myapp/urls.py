from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('data/', views.data, name='data'),  # Наши услуги
    path('test/', views.test, name='test'),  # Наши работы
    path('about/', views.about, name='about'),  # О компании
]








