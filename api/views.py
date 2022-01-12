from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import ColorPalette, FavouritePalette
from .serializers import ColorPaletteSerializer, FavouritePaletteSerializer
from .permissions import UpdateOwnColorPalette


class ColorPaletteListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Handle listing public color palette.
    """
    queryset = ColorPalette.objects.filter(is_public=True)
    serializer_class = ColorPaletteSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class ColorPaletteViewset(viewsets.ModelViewSet):
    """Handle create, read, update, delete color palette"""
    serializer_class = ColorPaletteSerializer
    permission_classes = [UpdateOwnColorPalette, IsAuthenticated]

    def perform_create(self, serializer):
        """Set the user to the logged in user"""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """listing the logged in user's color palette"""
        user = self.request.user
        return ColorPalette.objects.filter(user=user)


class AddFavouriteViewset(viewsets.ModelViewSet):
    """Handle create, update , delete favourite list"""

    serializer_class = FavouritePaletteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        favourite_queryset = FavouritePalette.objects.filter(user=user)
        if favourite_queryset.exists():
            raise ValidationError("You have already created your favourite list you can update or delete your list")
        serializer.save(user=user)

    def get_queryset(self):
        """Favourite list of logged in user"""
        return FavouritePalette.objects.filter(user=self.request.user)
