from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
  try:
    return dictionary.get(key)
  except AttributeError:
    return '' #bad for img

@register.filter
def split_item(url):
  return str(url).split("/",3)[-1]
    