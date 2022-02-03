from django.contrib import admin
from .models import Film


class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url_name': ('name', 'year_of_release')}


admin.site.register(Film, FilmAdmin)
