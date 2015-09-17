from django import template
from storage.models import DbFile

register = template.Library()

@register.assignment_tag
def dbfile_by_slug(slug):
    try:
        f = DbFile.objects.get(name = slug)
        return f
    except DbFile.DoesNotExist:
        return None
