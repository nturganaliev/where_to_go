from django.contrib import admin

from .models import Image, Place


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(Image)
