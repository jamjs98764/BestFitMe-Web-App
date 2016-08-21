"""Life insurance models."""

import enum

from django.db import models

from policies.models import company


class Policy(models.Model):
    """Generic description of a life insurance policy."""

    name = models.CharField(max_length=200)
    company = models.OneToOneField(company.Company)
    description = models.TextField()
    mortage = models.IntegerField()
    children_education_fund = models.IntegerField()
    critical_cover = models.IntegerField()


class Order(models.Model):
    """Policy selection with tweakble parameters set.
    
    Fields:
        cover_type: The type of cover
        cover_amount: amount compensated.
        premum_amount: term length in months.
    """

    cover_type = CoverType
    cover_amount = models.FloatField()
    premum_amount = models.IntegerField()
    policy = models.OneToOneField(Policy)


class CoverType(models.Model):
    class Meta:
        abstract = True


# TODO(fuyong): This is a bad name. Rename it.
class CoverKind(enum.Enum):
    CONSTANT = "CONSTANT"
    INCREASING = "INCREASING"
    DECREASING = "DECREASING"


class TermCover(CoverType):

    cover_kind = models.CharField(
            max_length=20,
            choices=list(CoverKind),
            default=CoverKind.CONSTANT)
    cover_level = models.IntegerField()
    term_length = models.IntegerField()


class LifeCover(CoverType):
    pass
