from django import template

register = template.Library()

@register.filter(name='filtro_boostrap')
def add_class(field, css_class):
    """Adds a class to a form field."""
    return field.as_widget(attrs={"class": css_class})
