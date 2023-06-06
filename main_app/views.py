from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Meme
import uuid
import boto3

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def meme_index(request):
  memes = Meme.objects.all()
  return render(request, 'memes/index.html', { 'memes': memes })

def meme_detail(request, meme_id):
  meme = Meme.objects.get(id=meme_id)
  return render(request, 'memes/detail.html', {'meme': meme})

class MemeCreate(CreateView):
  model = Meme
  fields = '__all__'
  success_url = '/memes/'

class MemeUpdate(UpdateView):
  model = Meme
  # Let's disallowmthe renaming of a Meme by excluding the name field!
  fields = '__all__'

class MemeDelete(DeleteView):
  model = Meme
  success_url = '/memes/'

def meme_canvas(request):
  return render(request, 'canvas.html')