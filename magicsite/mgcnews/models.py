from django.db import models

# Create your models here.
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from filebrowser.fields import FileBrowseField

from mgccms.models import article_base

class mlNews(article_base):
    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(mlNews, self).save(force_insert, force_update)
    class Meta:
        verbose_name        = _('news')
        verbose_name_plural = _('news')
    def get_absolute_url(self):
        return ('mgcnews_article', None, {
            'username': self.author.username,
            'year': self.publish.year,
            'month': "%02d" % self.publish.month,
            'slug': self.slug
    })

    # the article's url
    get_absolute_url = models.permalink(get_absolute_url)

from django import template
template.add_to_builtins('mgcnews.templatetags.mgcnews_tags')
