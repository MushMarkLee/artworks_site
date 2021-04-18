from django.contrib import admin
from django.conf import settings
from django.template.context_processors import static
from django.urls import path,include
from . import views

urlpatterns = [
                path(r'', views.artworks, name='artworks'),
                path('<int:pk>',views.ArtworksDetailView.as_view(), name='artwork-detail')
              ]