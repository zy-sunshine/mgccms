from django.template import Library

register = Library()

def render_paginate(context):
    if 'request' in context:
        getvars = context['request'].GET.copy()
        if 'page' in getvars:
            del getvars['page']
        if len(getvars.keys()) > 0:
            context.update({"getvars": "&%s" % getvars.urlencode()})
    
    # generate omit page_range
    half_num = 4
    num = half_num * 2 + 1
    if 'page_range' in context:
        page_cur = context['page']
        page_range_all = context['page_range']
        page_range = []
        page_num = context['pages']
        has_range_prev = False
        has_range_next = False
        if page_num <= num:
            page_range = page_range_all
        else:
            if page_cur >= 1 and page_cur <= half_num + 1:
                page_range = page_range_all[1:num]
                has_range_prev = False
                has_range_next = True
            if page_cur >= half_num + 2 and page_cur <= page_num - (half_num+1):
                page_range = page_range_all[page_cur-half_num:page+half_num]
                has_range_prev = True
                has_range_next = True
            if page_cur >= page_num - half_num and page_cur <= page_num:
                page_range = page_range_all[page_num-(num-1):page_num]
                has_range_prev = True
                has_range_next = False
        context.update({"page_range": page_range})
        context.update({"has_range_prev": has_range_prev})
        context.update({"has_range_next": has_range_next})
    return context
register.inclusion_tag('pagination/pagination.html', takes_context=True)(render_paginate)
