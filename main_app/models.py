from django.db import models
from django.urls import reverse

# Create your models here.

class Meme(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('meme-detail', kwargs={'meme_id': self.id})