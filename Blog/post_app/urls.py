from .views import render_all_posts
from django.urls import path


urlpatterns = [
    path("all_posts/", render_all_posts)
] 
