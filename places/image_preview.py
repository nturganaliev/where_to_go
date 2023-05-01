from django.utils.html import format_html


def image_preview(place):
    height = 200
    return format_html(
        "<img src={} height={} />",
        place.image.url,
        height
    )
