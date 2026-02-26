from django.db import models
from django.conf import settings

class Sighting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_by_id = models.IntegerField(null=True, blank=True)
    created_by_role = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.FileField(upload_to="sightings/", blank=True, null=True)

    def __str__(self):
        return f"{self.type} at ({self.latitude}, {self.longitude})"

class SightingConfirmation(models.Model):
    sighting = models.ForeignKey(Sighting, on_delete=models.CASCADE, related_name='confirmations')
    user_id = models.IntegerField()
    user_role = models.CharField(max_length=20)
    confirmed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['sighting', 'user_id'],
                name='unique_sighting_confirmation'
            )
        ]
