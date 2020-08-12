from django.contrib import admin
from .models import Incidences

# Register your models here.
class IncidenceAdmin(admin.ModelAdmin):
    list_display = (
        "name", "location"
    )
    
admin.site.register(Incidences, IncidenceAdmin)