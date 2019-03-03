from django.db import models

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =50)
    image = models.ImageField(upload_to = 'photos/')

    def __str__(self):
        return self.name
