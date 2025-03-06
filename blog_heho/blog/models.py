'''
Module containing the models for the blog
'''
from django.db import models

class BlogPost(models.Model):
    '''
    Model to store blog posts
    '''
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
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

    def __str__(self):
        '''
        String representation of the model
        '''
        return str(self.image)
