from django.contrib import admin

from .models import Image, Place


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ['image_preview',]

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    # fields = ['image_preview',]


admin.site.register(Image)
