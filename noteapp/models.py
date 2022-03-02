from django.db import models
from django.contrib.auth.models import User


class NoteModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
