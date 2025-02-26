from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all()  # Get all blog posts from the database
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail_view(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, "blog/blog_detail.html", {"post": post})

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # For now, just print the message (later, you can send an email or save to a database)
        print(f"New Contact Message from {name} ({email}): {message}")

        return HttpResponse("Thank you for your message!")

    return render(request, "contact.html")

def home_view(request):
    posts = BlogPost.objects.order_by('-id')[:5]  # Fetch the latest 5 blog posts
    return render(request, "home.html", {"posts": posts})
