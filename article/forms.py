from django import forms
from django.forms import ModelForm
from article.models import Document

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
