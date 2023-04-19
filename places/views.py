from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def index(request):
    features = []
    places = Place.objects.all()

    for place in places:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude],
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_details', args=(place.id,))
            }
        }
        features.append(feature)
    places_geojson = {
        'type': 'FeatureCollection',
        'features' : features
    }

    return render(request, 'index.html', context={'places_geojson': places_geojson})


def place_details(request, pk):
    place = get_object_or_404(Place, pk=pk)
    details = {
        'title': place.title,
        'images': [image.image.url for image in place.images.order_by('position')], 
        'description_short': place.description_short, 
        'description_long': place.description_long,
        'coordinates': {
            'longitude': place.longitude,
            'latitude': place.latitude
        }
    }
    return JsonResponse(details, json_dumps_params={'ensure_ascii':False, 'indent': 2})
