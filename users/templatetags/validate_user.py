from django import template
from django.utils.dateparse import datetime

register = template.Library()

@register.simple_tag
def validate_user(birthday):
    now = datetime.datetime.now()
    birth_year = birthday.year
    age = now.year - birth_year
    if (age > 13):
        result = "allowed"
    else:
        result = "blocked"
    return result
