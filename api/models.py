from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


class ColorPalette(models.Model):
    name = models.CharField(max_length=255)
    dominant_color = models.CharField(max_length=255)
    accent_color = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class FavouritePalette(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_palettes = models.ManyToManyField(ColorPalette)

    def __str__(self):
        return f'Favourites-{self.user.username}'
