from django.db import models
import os
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/', null=True)

    def __str__(self):
        return self.title