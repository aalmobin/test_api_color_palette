from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


class ColorPalette(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class DominantColor(models.Model):
    name = models.CharField(max_length=255)
    color_palette = models.ForeignKey(ColorPalette, related_name='dominant_colors', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AccentColor(models.Model):
    name = models.CharField(max_length=255)
    color_palette = models.ForeignKey(ColorPalette, related_name='accent_colors', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FavouritePalette(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_palettes = models.ManyToManyField(ColorPalette)

    def __str__(self):
        return f'Favourites-{self.user.username}'
