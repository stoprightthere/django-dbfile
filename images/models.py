from django.db import models
from storage.storage import DbStorage

storage = DbStorage()

class Image(models.Model):
    image = models.ImageField(storage = storage, upload_to='dummy')
