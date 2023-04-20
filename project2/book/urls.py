from django.contrib import admin
from django.urls import path,include
from book import views

urlpatterns = [
    path('',views.index,name='index'),
    path('detail/',views.detail,name='detail'),
]