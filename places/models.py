from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.db import models

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = HTMLField('Полное описание')
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Картинка')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images'
    )
    position = models.PositiveIntegerField('Позиция', default=0)

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f'{self.place.title}'

    def image_preview(self):
        width = 200
        return format_html(
            "<img src={} width={} />",
            self.image.url,
            width
        )