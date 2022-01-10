from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import ColorPalette, FavouritePalette


admin.site.register(ColorPalette, SimpleHistoryAdmin)
admin.site.register(FavouritePalette)
