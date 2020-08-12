from django.db import models

class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Incidences"