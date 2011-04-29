from django.db import models
from django.utils.translation import ugettext as _

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
    ('IT', _('Italy')),
    ('CY', _('Cyprus')),
    ('LV', _('Latvia')),
    ('LT', _('Lithuania')),
    ('LU', _('Luxembourg')),
    ('HU', _('Hungary')),
    ('MT', _('Malta')),
    ('NL', _('Netherlands')),
    ('AT', _('Austria')),
    ('PL', _('Poland')),
    ('PT', _('Portugal')),
    ('RO', _('Romania')),
    ('SI', _('Slovenia')),
    ('SK', _('Slovakia')),
    ('FI', _('Finland')),
    ('SE', _('Sweden')),
    ('UK', _('United Kingdom ')),
    )

RESOURCES = (
    ('1', _('port')),
    ('2', _('protocol')),
    ('3', _('service')),
    ('4', _('site')),
    ('5', _('user')),
    ('6', _('ip')),
    )
TYPES = (
    ('1', _('Blocking')),
    ('2', _('Throttling')),
    )
MEDIA = (
    ('1', _('Fixed')),
    ('2', _('Mobile')),
    )

class Attachment(models.Model):
    attachment = models.FileField(upload_to='static')

class Comment(models.Model):
    submitter = models.EmailField()
    comment = models.TextField()
    date = models.DateField()
    attachments = models.ForeignKey(Attachment)

class Violation(models.Model):
    country = models.CharField(max_length=2, choices=COUNTRIES)
    operator = models.CharField(max_length=256)
    contract = models.CharField(max_length=256)
    comments = models.ForeignKey(Comment)
    resource = models.CharField(max_length=1, choices=RESOURCES)
    type = models.CharField(max_length=1, choices=TYPES)
    media = models.CharField( max_length=1, choices=MEDIA)
    temporary = models.BooleanField( )
    contractual = models.BooleanField()
    contract_excerpt = models.TextField()
    loophole = models.BooleanField()
