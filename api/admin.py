from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import ColorPalette, FavouritePalette, AccentColor, DominantColor


admin.site.register(ColorPalette, SimpleHistoryAdmin)
admin.site.register(FavouritePalette)
admin.site.register(AccentColor)
admin.site.register(DominantColor)
