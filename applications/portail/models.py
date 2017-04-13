# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import datetime
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible
class Artefact(models.Model):
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

	ObjectName          = models.
	GeneralDescription  = models.
	model               = models.
	SerialNumber        = models.
	Manufacturer        = models.
	ManuCountry         = models.
	ManuProvince        = models.
	ManuCity            = models.
	BeginDate           = models.
	EndDate             = models.
	date_qualifier      = models.
	patent              = models.
	NumberOfComponents  = models.
	ArtifactFinish      = models.
	ContextCanada       = models.
	ContextFunction     = models.
	ContextTechnical    = models.
	group1              = models.
	category1           = models.
	subcategory1        = models.
	group2              = models.
	category2           = models.
	subcategory2        = models.
	group3              = models.
	category3           = models.
	subcategory3        = models.
	material            = models.
	Length              = models.
	Width               = models.
	Height              = models.
	Thickness           = models.
	Weight              = models.
	Diameter            = models.
	image               = models.
	thumbnail           = models.
	language = models.CharField(max_length=2, choices=LANGUAGE_CHOICE, default=ENGLISH)

    JOBURL = models.URLField(max_length=250, blank=True, null=True)
    EXPIRYDATE = models.DateField(auto_now=False, blank=True, null=True)
    SALARYMAX = models.CharField(max_length=40, blank=True, null=True)
    SALARYMIN = models.CharField(max_length=40, blank=True, null=True)
    SALARYTYPE = models.CharField(max_length=20, blank=True, null=True)
    NAME = models.CharField(max_length=40, blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICE, default=ENGLISH)
    POSITION = models.CharField(max_length=150, blank=True, null=True)
    JOBREF = models.CharField(max_length=30, unique=True, blank=True, null=True)
    JOB_SUMMARY = models.TextField(blank=True, null=True)
    POSTDATE = models.DateTimeField(auto_now=False, blank=True, null=True)
    slug = models.CharField(max_length=200)
    tweeted = models.BooleanField(default=False)

@python_2_unicode_compatible
class Description(models.Model):
    '''
    Job.Description.models
    '''
    def __str__(self):
        return self.COMPANY_DESC

    jobs = models.ForeignKey(Job, on_delete=models.CASCADE)
    KNOWLEDGE = models.TextField(blank=True, null=True)
    LANGUAGE_CERTIFICATES = models.TextField(blank=True, null=True)
    EDUCATIONANDEXP = models.TextField(blank=True, null=True)
    COMPANY_DESC = models.TextField(blank=True, null=True)
    POSTDATE = models.DateTimeField(auto_now=True, blank=True, null=True)
