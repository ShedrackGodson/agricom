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