from django import  forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'w-full p-4 border rounded-lg focus:ring-2 focus:ring-blue-500'}))
    email = forms.EmailField(validators=[EmailValidator()], widget=forms.TextInput(attrs={'class': 'w-full p-4 border rounded-lg focus:ring-2 focus:ring-blue-500'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'w-full p-4 border rounded-lg focus:ring-2 focus:ring-blue-500'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-full p-4 border rounded-lg focus:ring-2 focus:ring-blue-500'}))