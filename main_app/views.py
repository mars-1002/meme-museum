from django.shortcuts import render
from .models import Meme

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