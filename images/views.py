# -*- coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render

from .models import Image

def gallery(request):
    images = Image.objects.all()
    print images
    return render(request, 'gallery.html', {'images': images})
