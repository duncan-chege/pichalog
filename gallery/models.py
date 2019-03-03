from django.db import models

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =50)
    image = models.ImageField(upload_to = 'photos/')

    def __str__(self):
        return self.name

class Location(models.Model):
    lname = models.CharField(max_length =30)

    def __str__(self):
        return self.lname

class Category(models.Model):
    cname = models.CharField(max_length =30)

    def __str__(self):
        return self.cname




