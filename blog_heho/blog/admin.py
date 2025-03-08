'''
Admin page for the blog app
'''
from django.contrib import admin
from .models import BlogPost, BlogImage, Tag

admin.site.register(BlogPost)
admin.site.register(Tag)
admin.site.register(BlogImage)
