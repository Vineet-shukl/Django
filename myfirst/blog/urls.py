
from django.urls import path
from .views import blog_index
urlpatterns = [
    path('',blog_index),
   ]