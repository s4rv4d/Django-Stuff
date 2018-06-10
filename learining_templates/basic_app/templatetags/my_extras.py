from django import template

register = template.Library()

def cut(value,arg):
    # This cuts out all arg values from the string

    return value.replace(arg,'')

# register.filter('cut',cut)
# or
@register.filter(name="cut")
