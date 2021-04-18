from django.shortcuts import render, redirect
from .models import Artworks
from django.views.generic import DetailView

def artworks(request):
    artworks = Artworks.objects.all()
    return render(request, 'artworks/artworks.html',{'artworks':artworks})

class ArtworksDetailView(DetailView):
    model = Artworks
    template_name = 'artworks/artworks_detail.html'
    context_object_name = 'artwork'