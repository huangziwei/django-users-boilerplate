from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    name = models.CharField(verbose_name=_("name"), blank=True, max_length=255)
    bio = models.TextField("Bio", blank=True)
