from django.db import models

class Donnees(models.Model):
    datetime = models.DateTimeField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    humidite = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donnees'
