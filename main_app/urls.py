from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('memes/', views.meme_index, name='meme-index'),
  path('memes/<int:meme_id>/', views.meme_detail, name='meme-detail'),
  path('memes/create/', views.MemeCreate.as_view(), name='meme-create'),
  path('memes/<int:pk>/update/', views.MemeUpdate.as_view(), name='meme-update'),
  path('memes/<int:pk>/delete/', views.MemeDelete.as_view(), name='meme-delete'),
  path('memes/canvas/', views.meme_canvas, name='meme-canvas')
]