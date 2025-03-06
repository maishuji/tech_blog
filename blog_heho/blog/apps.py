'''
This file is used to configure the app.
'''
from django.apps import AppConfig

class BlogConfig(AppConfig):
    '''
    Class used to configure the app
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
