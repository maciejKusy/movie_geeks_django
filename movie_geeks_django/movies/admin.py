from django.contrib import admin

from .models import Film, FilmReview, Genre


class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url_name": ("name", "year_of_release")}


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url_name": ("name",)}


admin.site.register(Film, FilmAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(FilmReview)
