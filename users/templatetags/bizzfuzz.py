from django import template

register = template.Library()

@register.simple_tag
def bizzfuzz(random_number):
    result = random_number
    if random_number % 3 == 0:
        result = "Bizz"
    if random_number % 5 == 0:
        result = "Fuzz"
    if random_number % 15 == 0:
        result = "BizzFuzz"
    return result
