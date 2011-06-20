from django.contrib import admin
from bt import models

class ViolationAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Violation, ViolationAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Comment, CommentAdmin)

class AttachmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Attachment, AttachmentAdmin)

class ConfirmationAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Confirmation, ConfirmationAdmin)
