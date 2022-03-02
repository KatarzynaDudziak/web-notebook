from urllib import request
from django import forms

class NoteForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()