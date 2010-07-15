from django.contrib import admin
from attachments.admin import AttachmentInlines

class MyEntryOptions(admin.ModelAdmin):
    inlines = [AttachmentInlines]

