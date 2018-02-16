from django.db import models

from tinymce.models import HTMLField


class Page(models.Model):
    title = models.CharField(max_length=30, unique=True)
    content = HTMLField()

    def __str__(self):
        return self.title
