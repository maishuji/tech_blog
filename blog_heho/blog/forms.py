'''
Module containing the forms for the blog
'''
from django import  forms
from django.core.validators import EmailValidator
from .models import Comment

class ContactForm(forms.Form):
    '''
    Contact form class used to show a form to send an email to blog author
    '''
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-4 border rounded-lg focus:ring-2 focus:ring-blue-500'}
        )
    )
    email = forms.EmailField(
        validators=[EmailValidator()],
        widget=forms.TextInput(
            attrs={'class': 'w-full p-4 border rounded-lg focus:ring-2 focus:ring-blue-500'}
        )
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-4 border rounded-lg focus:ring-2 focus:ring-blue-500'}
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'w-full p-4 border rounded-lg focus:ring-2 focus:ring-blue-500'}
        )
    )

# pylint: disable=too-few-public-methods
class CommentForm(forms.ModelForm):
    '''
    Comment form class used to show a form to add a comment to a blog post'''
    class Meta:
        '''
        Meta class used to define the model and fields for the form
        '''
        model = Comment
        fields = ["author", "content"]
        widgets = {
            "author": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg " \
                    "focus:ring-2 focus:ring-blue-500 focus:outline-none",
                "placeholder": "Your Name"
            }),
            "content": forms.Textarea(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg " \
                    "focus:ring-2 focus:ring-blue-500 focus:outline-none",
                "rows": 4,
                "placeholder": "Write your comment here..."
            }),
        }
