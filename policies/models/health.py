"""Health insurance models."""

from django.db import models

from policies.models import company


class HealthPolicy(models.Model):

    name = models.CharField(max_length=200)
    company = models.OneToOneField(company.Company)
    description = models.TextField()
    clinic_gp_cover = models.IntegerField()
    accident_cover = models.IntegerField()
    acute_care_cover = 1
    speciality_drug_cover = 1
    overseas_cover = 1


class HealthOrder(models.Model):

    hospital_admission_cover = models.BooleanField()
    long_term_care = models.BooleanField()
    policy = models.OneToOneField(HealthPolicy)
