# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Cablemodems(models.Model):

    #__Cablemodems_FIELDS__
    customer_id = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    house_number = models.IntegerField(null=True, blank=True)
    house_number_suffix = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    cm_macaddress = models.CharField(max_length=255, null=True, blank=True)
    cluster_id = models.CharField(max_length=255, null=True, blank=True)
    cable_interface = models.CharField(max_length=255, null=True, blank=True)
    last_updated = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Cablemodems_FIELDS__END

    class Meta:
        verbose_name        = _("Cablemodems")
        verbose_name_plural = _("Cablemodems")



#__MODELS__END
