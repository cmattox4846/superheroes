from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.

class Superhero(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    secondary_ability = models.CharField(max_length=50)
    catch_phrase = models.CharField(max_length=50)
    image =models.ImageField(upload_to = 'superheroes_image' ,blank =True)

    def __str__(self):
        return self.name

