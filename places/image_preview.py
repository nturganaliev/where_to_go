from django.utils.html import format_html


def image_preview(image):
    height = 200
    return format_html(
        "<img src={} height={} />",
        image.image.url,
        height,
    )
