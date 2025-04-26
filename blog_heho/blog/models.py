'''
Module containing the models for the blog
'''
from django.db import models
from django.utils.text import slugify

class Tag(models.Model):
    '''
    Model to store blog tags
    '''
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        '''
        String representation of the model
        '''
        return str(self.name)

class BlogPost(models.Model):
    '''
    Model to store blog posts
    '''
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    objects = models.Manager()  # Explicitly define objects manager (not necessary, but for pylint)
    def __str__(self):
        '''
        String representation of the model
        '''
        return str(self.title)

class BlogImage(models.Model):
    '''
    Model to store blog images
    '''
    image = models.ImageField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()  # Fixes potential Pylint issues


    def __str__(self):
        '''
        String representation of the model
        '''
        return str(self.image)

class Comment(models.Model):
    '''
    Model to store blog comments
    '''
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()  # Fixes potential Pylint issues


    def __str__(self):
        '''
        String representation of the model
        '''
        return f"Comment by {self.author} on {getattr(self.post, 'title', 'Unknown Post')}"
