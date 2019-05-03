from django import template

register = template.Library()


@register.simple_tag
def query_replace(request, field, value):
    """GETのクエリパラメタを追加する"""
    url_dict = request.GET.copy()
    url_dict[field] = value
    return url_dict.urlencode()
