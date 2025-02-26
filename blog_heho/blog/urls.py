from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='articles'),
    path('articles', views.blog_list, name='articles'),
    path('home', views.home_view, name='home'),
    path('contact', views.contact_view, name='contact'),
    path("blog/<int:post_id>/", views.blog_detail_view, name="blog_detail"),
]
