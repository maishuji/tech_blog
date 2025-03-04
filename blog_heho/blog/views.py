from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from .forms import ContactForm
from django.shortcuts import redirect
import markdown

def blog_list(request):
    posts = BlogPost.objects.all()
    # Pagination: Show 5 posts per page
    paginator = Paginator(posts, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Convert each post's content from Markdown to HTML
    for post in page_obj:
        post.content = markdown.markdown(post.content, extensions=["extra", "fenced_code", "toc"])
    return render(request, 'blog/blog_list.html', {'page_obj': page_obj})

def blog_detail_view(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    post.content = markdown.markdown(post.content, extensions=["extra", "fenced_code", "toc"])
    return render(request, "blog/blog_detail.html", {"post": post})

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract the data from the form
            return redirect('success')
    
    form = ContactForm()
    return render(request, "contact.html", {'form': form})
            

def home_view(request):
    posts = BlogPost.objects.order_by('-id')[:5]  # Fetch the latest 5 blog posts

    # Convert each post's content from Markdown to HTML
    for post in posts:
        post.content = markdown.markdown(post.content, extensions=["extra", "fenced_code", "toc"])
    return render(request, "home.html", {"posts": posts})
