from django.contrib import admin
from tinymce.settings import JS_URL
from django.conf import settings

from django.core.urlresolvers import reverse
from tinymce.widgets import TinyMCE

from models import mlRelease, VerDown

class VerDownAdmin(admin.ModelAdmin):
    pass
#    model = VerDown
#    extra = 3



class mlReleaseAdmin(admin.ModelAdmin):
    #fields = (
    #    (None, {'fields': ('pub_date', 'question')}),
    #)
#    fields = (
#        (None, {'fields': ('question',)}),
#        ('Date information', {'fields': ('pub_date',), 'classes': 'collapse'}),
#    )
#    inlines = [VerDownAdmin,]
    filter_horizontal = ('ver_down', )  
    list_display        = ('title', 'publish', 'status')
    list_filter         = ('publish', 'status')
    search_fields       = ('title', 'tease')
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('tease'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(mlReleaseAdmin, self).formfield_for_dbfield(db_field, **kwargs)



admin.site.register(mlRelease, mlReleaseAdmin)
admin.site.register(VerDown, VerDownAdmin)
