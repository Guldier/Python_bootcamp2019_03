from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="authors/%Y/%m/%d")