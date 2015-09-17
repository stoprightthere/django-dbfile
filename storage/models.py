from django.db import models

class DbFile(models.Model):
    content = models.TextField()
    name = models.TextField()
    mimetype = models.TextField()
