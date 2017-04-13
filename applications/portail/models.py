# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import datetime
from django.utils import timezone
from model_utils.models import TimeStampedModel

# Create your models here.
@python_2_unicode_compatible
class Artefact(TimeStampedModel, models.Model):
    '''
    Job.models
    '''
    FRENCH = 'FR'
    ENGLISH = 'EN'
    LANGUAGE_CHOICE = (
            (FRENCH, 'Francais'),
            (ENGLISH, 'English'),
            )
    def __str__(self):
        return self.ObjectName

    ObjectName          = models.CharField(max_length=40, blank=True, null=True, default="No Name")
    GeneralDescription  = models.CharField(max_length=40, blank=True, null=True)
    model               = models.CharField(max_length=40, blank=True, null=True)
    SerialNumber        = models.CharField(max_length=40, blank=True, null=True)
    Manufacturer        = models.CharField(max_length=40, blank=True, null=True)
    ManuCountry         = models.CharField(max_length=40, blank=True, null=True)
    ManuProvince        = models.CharField(max_length=40, blank=True, null=True)
    ManuCity            = models.CharField(max_length=40, blank=True, null=True)
    BeginDate           = models.CharField(max_length=40, blank=True, null=True)
    EndDate             = models.CharField(max_length=40, blank=True, null=True)
    date_qualifier      = models.CharField(max_length=40, blank=True, null=True)
    patent              = models.CharField(max_length=40, blank=True, null=True)
    NumberOfComponents  = models.CharField(max_length=40, blank=True, null=True)
    ArtifactFinish      = models.TextField(blank=True, null=True)
    ContextCanada       = models.TextField(blank=True, null=True)
    ContextFunction     = models.TextField(blank=True, null=True)
    ContextTechnical    = models.TextField(blank=True, null=True)
    group1              = models.CharField(max_length=40, blank=True, null=True)
    category1           = models.CharField(max_length=40, blank=True, null=True)
    subcategory1        = models.CharField(max_length=40, blank=True, null=True)
    group2              = models.CharField(max_length=40, blank=True, null=True)
    category2           = models.CharField(max_length=40, blank=True, null=True)
    subcategory2        = models.CharField(max_length=40, blank=True, null=True)
    group3              = models.CharField(max_length=40, blank=True, null=True)
    category3           = models.CharField(max_length=40, blank=True, null=True)
    subcategory3        = models.CharField(max_length=40, blank=True, null=True)
    material            = models.CharField(max_length=40, blank=True, null=True)
    Length              = models.CharField(max_length=40, blank=True, null=True)
    Width               = models.CharField(max_length=40, blank=True, null=True)
    Height              = models.CharField(max_length=40, blank=True, null=True)
    Thickness           = models.CharField(max_length=40, blank=True, null=True)
    Weight              = models.CharField(max_length=40, blank=True, null=True)
    Diameter            = models.CharField(max_length=40, blank=True, null=True)
    image               = models.URLField(max_length=250, blank=True, null=True)
    thumbnail           = models.URLField(max_length=250, blank=True, null=True)
    language            = models.CharField(max_length=2, choices=LANGUAGE_CHOICE, default=ENGLISH)

    def get_absolute_url(self):
        return reverse('portail:artefact_detail', args=(self.id,))
    
    class Meta:
        #ordering = ["-created"]
        #ordering = ("?",)
        verbose_name = 'Artefact'
        verbose_name_plural = 'Artefacts'

