from django.db import models

# Create your models here.
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from filebrowser.fields import FileBrowseField

from mgccms.models import article_base

class mlProjects(article_base):
    img_src = FileBrowseField(_("Image (Format 48x48)"), max_length=200, format='Image', blank=True, null=True, default='none.jpg') 
    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(mlProjects, self).save(force_insert, force_update)
    class Meta:
        verbose_name        = _('project')
        verbose_name_plural = _('projects')
    def get_absolute_url(self):
        return ('mgcprojects_article', None, {
            'username': self.author.username,
            'year': self.publish.year,
            'month': "%02d" % self.publish.month,
            'slug': self.slug
    })

    # the article's url
    get_absolute_url = models.permalink(get_absolute_url)
    
from django import template
template.add_to_builtins('mgcprojects.templatetags.mgcprojects_tags')
