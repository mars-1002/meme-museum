from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Meme
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

# Add the following import
from django.http import HttpResponse

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def meme_index(request):
  memes = Meme.objects.all()
  return render(request, 'memes/index.html', { 'memes': memes })

@login_required
def meme_detail(request, meme_id):
  meme = Meme.objects.get(id=meme_id)
  return render(request, 'memes/detail.html', {'meme': meme})

class MemeCreate(LoginRequiredMixin, CreateView):
  model = Meme
  fields = ['title', 'image', 'description']
  success_url = '/memes/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class MemeUpdate(LoginRequiredMixin, UpdateView):
  model = Meme
  fields = ['title', 'description']

class MemeDelete(LoginRequiredMixin, DeleteView):
  model = Meme
  success_url = '/memes/'

def meme_canvas(request):
  return render(request, 'canvas.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('meme-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)