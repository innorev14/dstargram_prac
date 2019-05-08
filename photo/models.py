from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='timeline_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now='True')

    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
