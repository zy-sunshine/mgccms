from django.db import models

# Create your models here.
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from filebrowser.fields import FileBrowseField

from mgccms.models import markup_choices

class VerDown(models.Model):
    version = models.CharField(_('Version'), max_length=80)
    download_url = models.CharField(_('Download URL'), max_length=200)
    created_at      = models.DateTimeField(_('created at'), default=datetime.now)
    
    class Meta:
        ordering            = ('-created_at',)
        verbose_name        = _('Version and Download Urls')
        verbose_name_plural = _('Version and Download Urls')
        
    def __unicode__(self):
        return self.version

class mlRelease(models.Model):
    """Article abstract model."""
    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )
    title           = models.CharField(_('title'), max_length=200)
    author          = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related", verbose_name="author")
    creator_ip      = models.IPAddressField(_("IP Address of the Post Creator"), blank=True, null=True)
    tease           = models.TextField(_('tease'), blank=True)
    status          = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    publish         = models.DateTimeField(_('publish'), default=datetime.now)
    created_at      = models.DateTimeField(_('created at'), default=datetime.now)
    updated_at      = models.DateTimeField(_('updated at'), auto_now=True)
    markup          = models.CharField(_(u"Post Content Markup"), max_length=10,
                              choices=markup_choices,
                              null=True, blank=True)
    img_src_index = FileBrowseField(_("Index Image(Format 460x*)"), max_length=200, format='Image', blank=True, null=True, default='none.jpg')
    ver_down = models.ManyToManyField(VerDown, related_name="%(app_label)s_%(class)s_related", verbose_name = "Version and Download Urls")
    
    class Meta:
        ordering            = ('-publish',)
        get_latest_by       = 'publish'
        verbose_name        = _('mlRelease')
        verbose_name_plural = _('mlRelease')


    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return ('mgcindex_article', None, {
            'username': self.author.username,
            'year': self.publish.year,
            'month': "%02d" % self.publish.month,
            'slug': self.slug
    })

    # the article's url
    get_absolute_url = models.permalink(get_absolute_url)

    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(mlRelease, self).save(force_insert, force_update)

from django import template
template.add_to_builtins('mgcindex.templatetags.mgcindex_tags')

if 0:    
    cd_version = models.CharField(_('Official Version(CD)'), max_length=80)
    cd_downloadurl = models.CharField(_('Download URL'), max_length=200)
    uni_version = models.CharField(_('uni Version'), max_length=80)
    uni_downloadurl = models.CharField(_('Download URL'), max_length=200)
    nopae_version = models.CharField(_('NOPAE Version'), max_length=80)
    nopae_downloadurl = models.CharField(_('Download URL'), max_length=200)
    livecd_version = models.CharField(_('LIVECD Version'), max_length=80)
    livecd_downloadurl = models.CharField(_('Download URL'), max_length=200)
    kde3cd_version = models.CharField(_('Version'), max_length=80)
    kde3cd_downloadurl = models.CharField(_('Download URL'), max_length=200)
    kde4dvd_version = models.CharField(_('KDE4 DVD Version'), max_length=80)
    kde4dvd_downloadurl = models.CharField(_('Download URL'), max_length=200)