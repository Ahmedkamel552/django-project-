from django.urls import path
from . import views

urlpatterns = [path("", views.index),
               path("new", views.new),]  # mapping the views to urls
