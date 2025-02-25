from django.shortcuts import render
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all()  # Get all blog posts from the database
    return render(request, 'blog/blog_list.html', {'posts': posts})
