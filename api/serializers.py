from rest_framework import serializers
from . models import ColorPalette, FavouritePalette


class ColorPaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorPalette
        fields = ('id', 'user', 'name', 'is_public', 'dominant_color', 'accent_color')
        extra_kwargs = {'user': {'read_only': True}}


class FavouritePaletteSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavouritePalette
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}
