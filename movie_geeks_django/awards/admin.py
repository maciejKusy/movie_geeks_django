from django.contrib import admin
from .models import FilmAward, FilmAwardReceived

admin.site.register(FilmAward)
admin.site.register(FilmAwardReceived)
