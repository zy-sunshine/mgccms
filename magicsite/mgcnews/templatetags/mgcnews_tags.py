from django.template import Library
from django.conf import settings

from mgcnews.models import mlNews
register = Library()

# -----------------------------------------------
# *_top_digg
@register.inclusion_tag("mgccms/snippet/top_digg.html")
def news_top_digg():
    return {
            'news': mlNews.objects.filter(status=2).select_related(depth=1).order_by("-digg")[:10],
            }

# -----------------------------------------------
# *_last_article
@register.inclusion_tag("mgccms/snippet/last_articles.html")
def news_last_articles():
    news = mlNews.objects.filter(status=2).select_related(depth=1).order_by("-publish")
    return {
            'news': news[:5]
    }

from django.contrib import comments
from tagging.models import Tag, TaggedItem
from django.shortcuts import get_object_or_404
# -----------------------------------------------
# *_relate_tag_news  
@register.inclusion_tag("mgccms/snippet/relate_tag_articles.html")
def news_relate_tag_articles(num, news):
    tags = news.tags.split(',')
    relate_news = []
    for tag in tags:
        if tag:
            tag = get_object_or_404(Tag, name=tag)
            relate_news.extend(TaggedItem.objects.get_by_model(mlNews, tag))
    return {
            'news': relate_news[:num]
            }

# TODO
# def relate_title_news():

# -----------------------------------------------
# *_show_tags
@register.inclusion_tag("mgcnews/snippet/news_tag_list.html")
def news_show_tags_for_article(obj):
    return {"obj": obj}

# -----------------------------------------------
# *_month_links
@register.inclusion_tag("mgcnews/snippet/news_month_links.html")
def news_month_links():
    return {
            'dates': mlNews.objects.dates('publish', 'month')[:12],
            }
