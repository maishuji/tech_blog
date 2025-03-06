'''
Admin page for the blog app
'''
from django.contrib import admin
from .models import BlogPost, BlogImage

admin.site.register(BlogPost)
admin.site.register(BlogImage)
