from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.comments.moderation import CommentModerator, moderator

COUNTRIES = (
    ('BE', _('Belgium')),
    ('BG', _('Bulgaria')),
    ('CZ', _('Czech Republic')),
    ('DK', _('Denmark')),
    ('DE', _('Germany')),
    ('EE', _('Estonia')),
    ('IE', _('Ireland')),
    ('EL', _('Greece')),
    ('ES', _('Spain')),
    ('FR', _('France')),
    ('IS', _('Iceland')),
    ('IT', _('Italy')),
    ('CY', _('Cyprus')),
    ('LV', _('Latvia')),
    ('LT', _('Lithuania')),
    ('LU', _('Luxembourg')),
    ('HU', _('Hungary')),
    ('MT', _('Malta')),
    ('NL', _('Netherlands')),
    ('NO', _('Norway')),
    ('AT', _('Austria')),
    ('PL', _('Poland')),
    ('PT', _('Portugal')),
    ('RO', _('Romania')),
    ('SI', _('Slovenia')),
    ('SK', _('Slovakia')),
    ('FI', _('Finland')),
    ('SE', _('Sweden')),
    ('UK', _('United Kingdom')),
    )

RESOURCES = (
    ('port', _('port')),
    ('protocol', _('protocol')),
    ('service', _('service')),
    ('site', _('site')),
    ('user', _('user')),
    ('ip', _('ip')),
    )
TYPES = (
    ('blocking', _('Blocking')),
    ('throttling', _('Throttling')),
    )
MEDIA = (
    ('fixed', _('Fixed')),
    ('mobile', _('Mobile')),
    )
STATUS = (
    ('new', _('New')),
    ('duplicate', _('Duplicate')),
    ('verified', _('Verified')),
    ('moreinfo', _('Need more info')),
    ('ooscope', _('Out of scope')),
    )

class Violation(models.Model):
    country = models.CharField(max_length=2, choices=COUNTRIES)
    operator = models.CharField(max_length=256)
    contract = models.CharField(max_length=256, blank=True)
    resource = models.CharField(max_length=20, choices=RESOURCES, blank=True)
    resource_name = models.CharField(max_length=4096, blank=True)
    type = models.CharField(max_length=20, choices=TYPES, blank=True)
    media = models.CharField( max_length=20, choices=MEDIA, blank=True)
    temporary = models.BooleanField( )
    contractual = models.BooleanField()
    contract_excerpt = models.TextField(blank=True)
    loophole = models.BooleanField()
    activationid= models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=20, choices=STATUS, default='new', blank=True)
    editorial = models.TextField(blank=True)

    def confirmations(self):
        return self.confirmation_set.filter(key='').count()

    class Admin:
        pass

    def __unicode__(self):
        return "#%s %s/%s" % (self.pk, self.country, self.operator)


class Comment(models.Model):
    submitter_email = models.EmailField()
    submitter_name = models.CharField(max_length=20)
    comment = models.TextField()
    timestamp = models.DateTimeField()
    violation = models.ForeignKey(Violation)

    class Admin:
        pass

    def __unicode__(self):
        return _("Comment #%s") % (self.pk)

class Attachment(models.Model):
    storage = models.FileField(upload_to='static')
    name= models.CharField(max_length=512)
    type= models.CharField(max_length=512)
    comment = models.ForeignKey(Comment)

    class Admin:
        pass

    def __unicode__(self):
        return self.name

class Confirmation(models.Model):
    key=models.CharField(max_length=64, blank=True)
    email=models.EmailField()
    violation = models.ForeignKey(Violation)

    class Admin:
        pass

class ViolationModerator(CommentModerator):
    email_notification = True
    moderate_after        = 0
    def moderate(self, comment, content_object, request):
        return True

if Violation not in moderator._registry:
    moderator.register(Violation, ViolationModerator)

class FeaturedCase(models.Model):
    case = models.OneToOneField(Violation)

    class Admin:
        pass

    def __unicode__(self):
        return u"*%s*" % self.case
