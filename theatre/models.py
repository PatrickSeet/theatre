from django.db import models

# Create your models here.
class Theatre(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=50, null=True)
    cinema = models.ForeignKey(Theatre, related_name='cinema')

    def __unicode__(self):
        return self.name

class Showtime(models.Model):
    time = models.IntegerField()
    movie = models.ForeignKey(Movie, related_name='movie')

    def __unicode__(self):
        return self.time