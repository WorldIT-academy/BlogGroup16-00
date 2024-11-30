from django.shortcuts import render
from .models import Post


def render_all_posts(request):

    all_posts = Post.objects.all()

    return render(
        template_name = "post_app/all_posts.html", 
        request = request,
        context = {
            'all_posts': all_posts
        }
        )