from django.db import models

# Create your models here.
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from filebrowser.fields import FileBrowseField

try:
    markup_choices = settings.WIKI_MARKUP_CHOICES  # reuse this for now; taken from wiki
except AttributeError:
    markup_choices = (
        ('html', _(u'Html')),
        ('rst', _(u'reStructuredText')),
        ('txl', _(u'Textile')),
        ('mrk', _(u'Markdown')),
    )

class article_base(models.Model):
    """Post model."""
    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )
    title           = models.CharField(_('title'), max_length=200)
    slug            = models.SlugField(_('slug'))
    author          = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related", verbose_name="the article author")
    creator_ip      = models.IPAddressField(_("IP Address of the Post Creator"), blank=True, null=True)
    body            = models.TextField(_('body'))
    tease           = models.TextField(_('tease'), blank=True)
    status          = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    allow_comments  = models.BooleanField(_('allow comments'), default=True)
    publish         = models.DateTimeField(_('publish'), default=datetime.now)
    created_at      = models.DateTimeField(_('created at'), default=datetime.now)
    updated_at      = models.DateTimeField(_('updated at'), auto_now=True)
    markup          = models.CharField(_(u"Post Content Markup"), max_length=10,
                              choices=markup_choices,
                              null=True, blank=True)

    
    class Meta:
        verbose_name        = _('post')
        verbose_name_plural = _('posts')
        ordering            = ('-publish',)
        get_latest_by       = 'publish'
        abstract = True

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('dpress_post', None, {
            'username': self.author.username,
            'year': self.publish.year,
            'month': "%02d" % self.publish.month,
            'slug': self.slug
    })

    # the article's url
    url = models.permalink(get_absolute_url)


class mlNews(article_base):
    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(mlNews, self).save(force_insert, force_update)
    #news_category = models.CharField(_('Download URL'), max_length=200)
    def get_category_url(self):
        return ('dpress_post', None, {
            'category': self.news_category,
    })
    #category_url = models.permalink(get_category_url)
    
class mlHistory(article_base):
    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(mlHistory, self).save(force_insert, force_update)