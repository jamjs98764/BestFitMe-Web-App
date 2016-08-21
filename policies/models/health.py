"""Health insurance models."""

from django.db import models

from policies.models import company


class Policy(models.Model):

    name = models.CharField(max_length=200)
    company = Ref[]
    description = models.TextField()
    clinic_gp_cover = models.IntegerField()
    accident_cover = models.IntegerField()
    acute_care_cover = 1
    speciality_drug_cover = 1
    overseas_cover = 1


class Order(models.Model):

    hospital_admission_cover = models.BooleanField()
    long_term_care = models.BooleanField()
    policy = models.OneToOneField(Policy)
