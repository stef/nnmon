from django.contrib import admin
from bt import models

class CommentInline(admin.TabularInline):
   model = models.Comment
   max_num = 1

class ViolationAdmin(admin.ModelAdmin):
   list_display = ('state', 'country', 'operator', 'contract', 'resource_name', 'media', 'activationid')
   list_filter = ('state', 'operator_ref', 'contract', 'resource_name', 'media', 'country')
   inlines = [CommentInline, ]
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
   list_filter = ('violation__operator_ref', 'violation__contract', 'violation__resource_name', 'violation__media', 'violation__country')
admin.site.register(models.Confirmation, ConfirmationAdmin)

class FeaturedCaseAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.FeaturedCase, FeaturedCaseAdmin)

class OperatorAdmin(admin.ModelAdmin):
   list_display = ("__unicode__", "reported_violations")
   search_fields = ('name', )
   pass
admin.site.register(models.Operator, OperatorAdmin)