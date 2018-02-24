# Django core
from django.db import models

# Third party
from djrichtextfield.models import RichTextField


class Page(models.Model):
    title = models.CharField(max_length=30, unique=True)
    content = RichTextField()

    def __str__(self):
        return self.title
