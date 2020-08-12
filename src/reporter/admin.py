from django.contrib import admin
from .models import Incidences, Districts, Regions, County, Ward, TZAll
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class IncidenceAdmin(LeafletGeoAdmin):
    list_display = (
        "name", "location"
    )

class DistrictsAdmin(LeafletGeoAdmin):
    list_display = (
        "district_n", "district_c", "geom"
    )

class RegionsAdmin(LeafletGeoAdmin):
    list_display = (
    "region_cod", "region_nam", "geom"
)

admin.site.register(Incidences, IncidenceAdmin)
admin.site.register(Districts, DistrictsAdmin)
admin.site.register(Regions, RegionsAdmin)
admin.site.register(County)
admin.site.register(Ward)
admin.site.register(TZAll)