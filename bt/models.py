from django.db import models

COUNTRIES = (
    ('BE', 'Belgium'),
    ('BG', 'Bulgaria'),
    ('CZ', 'Czech Republic'),
    ('DK', 'Denmark'),
    ('DE', 'Germany'),
    ('EE', 'Estonia'),
    ('IE', 'Ireland'),
    ('EL', 'Greece'),
    ('ES', 'Spain'),
    ('FR', 'France'),
    ('IT', 'Italy'),
    ('CY', 'Cyprus'),
    ('LV', 'Latvia'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
    ('HU', 'Hungary'),
    ('MT', 'Malta'),
    ('NL', 'Netherlands'),
    ('AT', 'Austria'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('RO', 'Romania'),
    ('SI', 'Slovenia'),
    ('SK', 'Slovakia'),
    ('FI', 'Finland'),
    ('SE', 'Sweden'),
    ('UK', 'United Kingdom '),
    )

class Attachment(models.Model):
    attachment = models.FileField(upload_to='static')

class Comment(models.Model):
    submitter = models.EmailField()
    comment = models.TextField()
    date = models.DateField()
    attachments = models.ForeignKey(Attachment)

class Violation(models.Model):
    RESOURCES = (
        ('1', 'port'),
        ('2', 'protocol'),
        ('3', 'service'),
        ('4', 'site'),
        ('5', 'user'),
        ('6', 'ip'),
    )
    TYPES = (
        ('1', 'Blocking'),
        ('2', 'Throttling'),
    )
    MEDIA = (
        ('1', 'Fixed'),
        ('2', 'Mobile'),
    )
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
