"""Various models for policies."""

import enum

from django.db import models


# ===============================
# Models shared by both policies
# ===============================


class Company(models.Model):
    name = models.CharField(max_length=200)


class CoverType(models.Model):
    class Meta:
        abstract = True


class CoverKind(enum.Enum):
    CONSTANT = 'CONSTANT'
    INCREASING = 'INCREASING'
    DECREASING = 'DECREASING'


class TermCover(CoverType):

    cover_kind = models.CharField(
            max_length=20,
            choices=[(str(kind), str(kind)) for kind in CoverKind],
            default=str(CoverKind.CONSTANT))
    cover_level = models.IntegerField()
    term_length = models.IntegerField()


class ForeverCover(CoverType):
    pass


# ===============================
# Models for Life Insurance
# ===============================


class LifePolicy(models.Model):
    """Generic description of a life insurance policy."""

    name = models.CharField(max_length=200)
    company = models.OneToOneField(Company)
    description = models.TextField()
    mortage = models.IntegerField()
    children_education_fund = models.IntegerField()
    critical_cover = models.IntegerField()



class LifePolicyOrder(models.Model):
    """Policy selection with tweakble parameters set.
    
    Fields:
        cover_type: The type of cover
        cover_amount: amount compensated.
        premum_amount: term length in months.
    """

    cover_type = CoverType
    cover_amount = models.FloatField()
    premum_amount = models.IntegerField()
    policy = models.OneToOneField(LifePolicy)


# ===============================
# Models for Health Insurance
# ===============================


class HealthPolicy(models.Model):

    name = models.CharField(max_length=200)
    company = models.OneToOneField(Company)
    description = models.TextField()
    clinic_gp_cover = models.IntegerField()
    accident_cover = models.IntegerField()
    acute_care_cover = 1
    speciality_drug_cover = 1
    overseas_cover = 1


class HealthPolicyOrder(models.Model):

    hospital_admission_cover = models.BooleanField()
    long_term_care = models.BooleanField()
    policy = models.OneToOneField(HealthPolicy)
