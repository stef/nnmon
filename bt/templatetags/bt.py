from django.template import Library, Variable
from django.conf import settings
from django import template
import random
from nnmon.bt.models import COUNTRIES, STATUS

register = Library()

@register.simple_tag
def root_url():
    return settings.ROOT_URL

@register.simple_tag
def media_url():
    return settings.MEDIA_URL

country_map=dict(COUNTRIES)
@register.filter(name='country')
def country(code):
    return country_map[code]

status_map=dict(STATUS)
@register.filter(name='status')
def status(code):
    return status_map[code]
