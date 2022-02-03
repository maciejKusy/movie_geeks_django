from django.contrib import admin
from .models import FilmAward, FilmAwardReceived


class FilmAwardAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url_name': ['name']}


class FilmAwardReceivedAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url_name': ('name', 'awarded_on', 'recipient')}


admin.site.register(FilmAward, FilmAwardAdmin)
admin.site.register(FilmAwardReceived, FilmAwardReceivedAdmin)
