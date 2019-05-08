from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Photo

# Create your views here.
class PhotoList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'

class PhotoCreate(CreateView):
    model = Photo
    fields = ['image', 'text']
    template_name = 'photo/photo_create.html'
    success_url = '/'

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['image', 'text']
    template_name = 'photo/photo_update.html'

class PhotoDetail(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'

class PhotoDelete(DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = '/'




