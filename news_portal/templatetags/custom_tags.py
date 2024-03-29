from datetime import datetime
import django.template
from pprint import pprint

register=django.template.Library()

@register.simple_tag()
def current_date(value):
    return datetime.strptime(value, "%d.%M.%Y")

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   pprint(f'request_context={context['request']}')
   print(f'request_context={context['request']}')
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()