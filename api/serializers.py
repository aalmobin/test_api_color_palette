from rest_framework import serializers
from . models import ColorPalette, FavouritePalette, DominantColor, AccentColor


class DominantColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DominantColor
        fields = ['name']


class AccentColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccentColor
        fields = ['name']


class ColorPaletteSerializer(serializers.ModelSerializer):
    dominant_colors = DominantColorSerializer(many=True)
    accent_colors = AccentColorSerializer(many=True)

    class Meta:
        model = ColorPalette
        fields = ['id', 'user', 'name', 'is_public', 'dominant_colors', 'accent_colors']
        extra_kwargs = {'user': {'read_only': True}}

    def create(self, validated_data):
        dominant_colors_data = validated_data.pop('dominant_colors')
        accent_colors_data = validated_data.pop('accent_colors')
        color_palette = ColorPalette.objects.create(**validated_data)
        for dominant_color_data in dominant_colors_data:
            DominantColor.objects.create(color_palette=color_palette, **dominant_color_data)
        for accent_color_data in accent_colors_data:
            AccentColor.objects.create(color_palette=color_palette, **accent_color_data)
        return color_palette


class FavouritePaletteSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavouritePalette
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}
