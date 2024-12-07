from .views import *
from django.urls import path


urlpatterns = [
    path("all_posts/", render_all_posts),
    path("view_post/<int:pk>", render_view_post)
] 
