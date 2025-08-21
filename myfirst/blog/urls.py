
from django.urls import path
from .views import blog_index, get_post,create_post,content_post,home,post_update,post_delete

urlpatterns = [
    path('', blog_index, name='blog_index'),
    path('post/',home, name='home'),
    path('posts/',get_post),
    path('posts/new',create_post),
    path('posts/new_post',content_post,name='content_post'),
    path('post/<int:pk>/edit/',post_update, name='post_update'),
    path('post/<int:pk>/delete/',post_delete, name='post_delete'),
   ]