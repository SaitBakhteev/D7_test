import crispy_forms.layout
from django.contrib.auth import forms
from django.template.defaultfilters import register, stringfilter
from crispy_forms.templatetags.crispy_forms_filters import register as crispy_forms_register


@register.filter
def censor(value,arg):
    try:
        if not isinstance(arg, str): # если аргумент не строкового типа, то вызывается исключение
            raise TypeError('Заменяемое значение должно быть строкой')
        return str(value).replace(arg,"*")
    except TypeError as e:
        print(str(e))
        return value

@crispy_forms_register.filter()
def crisp_HTML(value):
    return value
