from django.db import models
from datetime import datetime
from django.urls import reverse


# Create your models here.
class BlogPost(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.TextField()
    date = models.DateTimeField(default=datetime.now())

    def get_absolute_url(self):
        return reverse("blogpost-detail", kwargs={"id": self.id})
        # возвращает ссылку типа http://127.0.0.1:8000/database/1/
        # из urls.py:
        # path('database/<int:id>/', dynamic_lookup_view, name="blogpost-detail"),
