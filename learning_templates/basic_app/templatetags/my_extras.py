from django import template

register = template.Library()

@register.filter()
def cutt(value,arg):
    #This cuts out all the values of "arg" from the string
    return value.replace(arg,'')

# register.filter("cutt", cutt)
