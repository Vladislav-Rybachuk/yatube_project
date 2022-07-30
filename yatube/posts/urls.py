# posts/urls.py
from django.urls import path

from . import views

urlpattern= [
    path('',views.index),
    path('group/<slug:slug>/', views.group_posts),
]