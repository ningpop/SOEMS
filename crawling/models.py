from django.db import models

# Create your models here.

class Taling(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    