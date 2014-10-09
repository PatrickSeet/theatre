from django.contrib import admin
from theatre.models import Theatre
from theatre.models import Movie
from theatre.models import Showtime
# Register your models here.
admin.site.register(Theatre)
admin.site.register(Movie)
admin.site.register(Showtime)
