from django.contrib import admin
from adminsortable2.admin import SortableAdminBase
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Image, Place
from .image_preview import image_preview


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = [image_preview, ]


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = [image_preview, ]
