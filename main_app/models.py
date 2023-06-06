from django.db import models

# Create your models here.

class Meme(models.Model):
    title = models.CharField(max_length=100)
    image = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return self.title