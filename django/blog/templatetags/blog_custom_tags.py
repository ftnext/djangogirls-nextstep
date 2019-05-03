from django import template

register = template.Library()


@register.filter(is_safe=True)
def parse_keyword(querydict):
    """GETのクエリパラメタからkeyword(検索語句)を取り出す"""
    keyword = querydict.get('keyword')
    return keyword if keyword else ''


@register.simple_tag
def query_replace(request, field, value):
    """GETのクエリパラメタを追加する"""
    url_dict = request.GET.copy()
    url_dict[field] = value
    return url_dict.urlencode()
