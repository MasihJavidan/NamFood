from django import forms
from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea, required=True)
