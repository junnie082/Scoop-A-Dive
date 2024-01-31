import markdown
from django import template
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    
    return mark_safe(markdown.markdown(value, extensions=extensions))


@register.filter(name='calculate_duration')
def calculate_duration(time_in, time_out):
    if time_in and time_out: 
        # Convert time values to datetime objects
        time_in = datetime.strptime(str(time_in), '%H:%M:%S')
        time_out = datetime.strptime(str(time_out), '%H:%M:%S')

        # Calculate duration
        duration = time_out - time_in
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        return '{:02}:{:02}'.format(hours, minutes)
    return ''
