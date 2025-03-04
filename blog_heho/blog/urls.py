from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.blog_list, name='articles'),
    path('articles', views.blog_list, name='articles'),
    path('home', views.home_view, name='home'),
    path('contact', views.contact_view, name='contact'),
    path("blog/<int:post_id>/", views.blog_detail_view, name="blog_detail"),
    path('/success', TemplateView.as_view(template_name='success.html'), name='success')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
