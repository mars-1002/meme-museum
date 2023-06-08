from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Meme(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='media/')
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('meme-detail', kwargs={'meme_id': self.id})