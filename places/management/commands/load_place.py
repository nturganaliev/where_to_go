import requests

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Loads places to the place project database'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_url', type=str, help='Ссылка на данные с местом на карте'
        )

    def handle(self, *args, **kwargs):
        file_url = kwargs['file_url']

        response = requests.get(file_url)
        response.raise_for_status()
        content = response.json()

        new_place = Place.objects.create(
            title=content['title'],
            description_short=content['description_short'],
            description_long=content['description_long'],
            longitude=content['coordinates']['lng'],
            latitude=content['coordinates']['lat']
        )
        new_place.save()

        images_url = content['imgs']
        for index, image_url in enumerate(images_url, 1):
            image_name = image_url.split('/')[-1]
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            image = ContentFile(image_response.content)
            new_image, _ = Image.objects.get_or_create(
                place=new_place,
                image=image_name,
                position=index,
            )
            new_image.save()
            new_image.image.save(image_name, image, save=True)
