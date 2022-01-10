from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list-color-palette', views.ColorPaletteListViewSet, basename='list-color-palette')
router.register('colorpalette', views.ColorPaletteViewset, basename='colorplette')
router.register('add-favourite', views.AddFavouriteViewset, basename='add-favourite')


urlpatterns = [
    path('', include(router.urls)),
]
