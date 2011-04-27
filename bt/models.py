from django.db import models

# Create your models here.

class Attachment(models.Model):
    attachment = models.FileField(upload_to='static')

class Comment(models.Model):
    submitter = models.EmailField()
    comment = models.TextField()
    date = models.DateField()
    attachments = models.ForeignKey(Attachment)

class Violation(models.Model):
    COUNTRIES = (
        # TODO complete and sort
        ('A', 'Austria'),
        ('B', 'Belgium'),
        ('CZ', 'Czech Republic'),
        ('HU', 'Hungary'),
        ('RO', 'Romania'),
        ('SE', 'Sweden'),
        ('PL', 'Poland'),
        ('ES', 'Spain'),
        ('PT', 'Portugal'),
        ('I', 'Italy'),
        ('DE', 'Germany'),
        ('SK', 'Slovakia'),
        ('FR', 'France'),
    )
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
    country = models.CharField(max_length=2,
                               choices=COUNTRIES,
                               help_text='',
                               )
    operator = models.CharField(max_length=256,
                                help_text='')
    contract = models.CharField(max_length=256,
                                help_text='type of offer, i.e. the name of the subscription')
    comments = models.ForeignKey(Comment,
                                 help_text='')
    resource = models.CharField(blank=True,
                                max_length=1,
                                choices=RESOURCES,
                                help_text='')
    type = models.CharField(blank=True,
                            max_length=1,
                            choices=RESOURCES,
                            help_text='')
    media = models.CharField(blank=True,
                             max_length=1,
                             choices=MEDIA,
                             help_text='')
    temporary = models.BooleanField(blank=True,
                                    help_text='')
    contractual = models.BooleanField(blank=True,
                                      help_text='')
    contract_excerpt = models.TextField(blank=True,
                                        help_text='')
    loophole = models.BooleanField(blank=True,
                                   help_text='')
