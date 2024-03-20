from django.db import models
from django.utils.text import slugify


# Create your models here.
class Slider(models.Model):
    headline= models.CharField(max_length=400)
    subheadline = models.CharField(max_length=400)
    bio = models.CharField(max_length=400)
    image = models.ImageField(upload_to='slider_images/')

    def __str__(self):
        return self.headline


class MenuCategory(models.Model):
    name = models.CharField(max_length=400)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    dish_name = models.CharField(max_length=100)
    dish_description = models.CharField(max_length=400)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    categories = models.ForeignKey('MenuCategory',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/',default=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.dish_name

