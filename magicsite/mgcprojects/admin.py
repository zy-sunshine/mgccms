from django.contrib import admin
from tinymce.settings import JS_URL
from django.conf import settings

from django.core.urlresolvers import reverse
from tinymce.widgets import TinyMCE

from models import mlProjects
class mlProjectsAdmin(admin.ModelAdmin):
    list_display        = ('title', 'publish', 'status')
    list_filter         = ('publish', 'status')
    search_fields       = ('title', 'body', 'tease')
    prepopulated_fields = {'slug': ('title',)}
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('body', 'tease'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 150, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(mlProjectsAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(mlProjects, mlProjectsAdmin)