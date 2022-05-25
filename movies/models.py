from pyexpat import model
from statistics import mode
# from typing_extensions import Required
from django.db import models

# Create your models here.
class Cast(models.Model):
    name = models.CharField(max_length=20, blank=False)
    gender = models.CharField(max_length=1, blank=False)
    age = models.IntegerField(blank=False)

    def natural_key(self):
        return (self.name, self.gender, self.age)

    class Meta:
        ordering = ['name', 'gender', 'age']

    def __str__(self):
        return "Cast_Name : {}, Cast_Gender : {}, Cast_Age : {}".format(self.name, self.gender, self.age)

class Director(models.Model):
    name = models.CharField(max_length=20, blank=False)
    gender = models.CharField(max_length=1, blank=False)
    age = models.IntegerField(blank=False)

    class Meta:
        ordering = ['name', 'gender', 'age']

    def __str__(self):
        return "Director_Name : {}, Director_Gender : {}, Director_Age : {}".format(self.name, self.gender, self.age)
class Genre(models.Model):
    name = models.CharField(max_length=20, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return "Movie_Genre : {}".format(self.genre)
        
class Movie(models.Model):
    # id = models.CharField(max_length=10, primary_key=True)
    
    name = models.CharField(max_length=50, unique=True)
    reldate = models.IntegerField(blank=False)
    genre = models.ManyToManyField(Genre)
    cast = models.ManyToManyField(Cast)
    director = models.ManyToManyField(Director)


    class Meta:
        ordering = ['name', 'reldate']

    def __str__(self):
        return "Movie_name : {},  Movie_reldate : {}, Movie_genre : {}, Movie_cast : {}, Movie_director : {}".format(self.name,self.reldate , self.genre,self.cast, self.director)


