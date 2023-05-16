from django.db import models


class BikeStation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
