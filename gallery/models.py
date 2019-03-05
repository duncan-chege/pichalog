from django.db import models
import datetime as dt


class Location(models.Model):
    lname = models.CharField(max_length=30)

    def __str__(self):
        return self.lname

    def save_location(self):
        self.save()

class Category(models.Model):
    cname = models.CharField(max_length=30)

    def __str__(self):
        return self.cname

    class Meta:  # Meta subclass specifies model-specific options. This helps in ordering data
        verbose_name_plural = 'Categories'

    def save_category(self):
        self.save()


class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    image_path = models.ImageField(upload_to='photos/')
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def search_by_category(cls,search_term):         #search for an image using its category.
        search_result = cls.objects.filter(image_category__cname__icontains=search_term)
        return search_result

    @classmethod
    def get_image_by_id(cls,input_id):
        retrieved_image = cls.objects.get(id=input_id)
        return retrieved_image