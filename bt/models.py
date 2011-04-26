from django.db import models

# Create your models here.

class Attachment(models.Model):
    attachment = models.EmailField()

class Comment(models.Model):
    submitter = models.EmailField()
    comment = models.TextField()
    comments = models.ForeignKey(Comment)

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
    country = models.CharField(max_length=2, choices=COUNTRIES)
    operator = models.CharField()
    contract = models.CharField()
    comments = models.ForeignKey(Comment)
    resource = models.CharField(max_length=1, choices=RESOURCES)
    type = models.CharField(max_length=1, choices=RESOURCES)
    media = models.CharField(max_length=1, choices=MEDIA)
    temporary = models.BooleanField()
    contractual = models.BooleanField()
    contract = models.TextField()
    loophole = models.BooleanField()
