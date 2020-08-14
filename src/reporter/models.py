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
    district_c = geomodel.CharField(max_length=50)
    district_n = geomodel.CharField(max_length=50)
    geom = geomodel.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.district_c


class Regions(models.Model):
    region_cod = models.CharField(max_length=50)
    region_nam = models.CharField(max_length=50)
    geom = geomodel.MultiPolygonField(srid=4326)


class County(models.Model):
    objectid = geomodel.IntegerField()
    area = geomodel.FloatField()
    perimeter = geomodel.FloatField()
    county3_field = geomodel.FloatField()
    county3_id = geomodel.FloatField()
    county = geomodel.CharField(max_length=20)
    shape_leng = geomodel.FloatField()
    shape_area = geomodel.FloatField()
    geom = geomodel.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.area

class Ward(models.Model):
    et_id = geomodel.BigIntegerField()
    adm0_en = geomodel.CharField(max_length=50)
    adm0_sw = geomodel.CharField(max_length=50)
    adm0_pcode = geomodel.CharField(max_length=50)
    adm1_en = geomodel.CharField(max_length=50)
    adm1_pcode = geomodel.CharField(max_length=50)
    adm2_en = geomodel.CharField(max_length=50)
    adm2_pcode = geomodel.CharField(max_length=50)
    adm3_en = geomodel.CharField(max_length=50)
    adm3_pcode = geomodel.CharField(max_length=50)
    geom = geomodel.MultiPolygonField(srid=4326)
    objects = geomodel.Manager()

    def __str__(self):
        return self.et_id


# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class TZAll(models.Model):
    et_id = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True)
    et_left = models.BigIntegerField()
    et_right = models.BigIntegerField()
    adm3_l = models.CharField(max_length=50)
    adm2_l = models.CharField(max_length=50)
    adm1_l = models.CharField(max_length=50)
    adm0_l = models.CharField(max_length=50)
    admlevel = models.IntegerField()
    adm0_r = models.CharField(max_length=50)
    adm1_r = models.CharField(max_length=50)
    adm2_r = models.CharField(max_length=50)
    adm3_r = models.CharField(max_length=50)
    geom = models.MultiLineStringField(srid=4326)
    objects = geomodel.Manager()


    def __str__(self):
        return self.et_id

class Wards(models.Model):
    region_cod = models.CharField(max_length=50)
    region_nam = models.CharField(max_length=50)
    district_c = models.CharField(max_length=50)
    district_n = models.CharField(max_length=50)
    ward_code = models.CharField(max_length=50)
    ward_name = models.CharField(max_length=50)
    division = models.CharField(max_length=50, null=True)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = geomodel.MultiPolygonField(srid=4326)


class Waterbodies(models.Model):
    district = models.CharField(max_length=30)
    area = models.FloatField()
    perimeter = models.FloatField()
    tz_05g_field = models.FloatField()
    region = models.CharField(max_length=30)
    ward = models.CharField(max_length=40)
    status = models.CharField(max_length=20)
    lakes = models.CharField(max_length=25)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = geomodel.MultiPolygonField(srid=4326)