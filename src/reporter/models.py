from django.db import models
from django.contrib.gis.db import models as geomodel

class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = geomodel.PointField(srid=4326)
    objects = geomodel.Manager()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Incidences"


class Districts(models.Model):
    # python manage.py ogrinspect reporter/data/Districts.shp Districts --srid=4326 --mapping --multi
    district_c = models.CharField(max_length=50)
    district_n = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.district_c
    