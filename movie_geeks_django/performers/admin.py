from django.contrib import admin

from .models import Performer


class PerformerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url_name": ["full_name"]}


admin.site.register(Performer, PerformerAdmin)
