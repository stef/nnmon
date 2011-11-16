from django.contrib import admin
from bt import models

class ViolationAdmin(admin.ModelAdmin):
   list_display = ('state', 'country', 'operator', 'contract', 'resource_name', 'media', 'activationid')
   list_filter = ('state', 'operator', 'contract', 'resource_name', 'media', 'country')
admin.site.register(models.Violation, ViolationAdmin)

class CommentAdmin(admin.ModelAdmin):
   list_display = ('violation', 'submitter_name', 'comment')
   list_filter = ('violation', 'submitter_name')
admin.site.register(models.Comment, CommentAdmin)

class AttachmentAdmin(admin.ModelAdmin):
   list_display = ('name', 'comment')
admin.site.register(models.Attachment, AttachmentAdmin)

class ConfirmationAdmin(admin.ModelAdmin):
   list_display = ('violation', 'key')
   list_filter = ('violation__operator', 'violation__contract', 'violation__resource_name', 'violation__media', 'violation__country')
admin.site.register(models.Confirmation, ConfirmationAdmin)

class FeaturedCaseAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.FeaturedCase, FeaturedCaseAdmin)
