import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""

    id = models.UUIDField(_('id'), unique=True,
                          primary_key=True, default=uuid.uuid4())
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('phone'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    avatar = models.ImageField(
        _('avatar'), upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        """Meta definition for User."""

        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'user'

    def __str__(self):
        """Unicode representation of User."""
        return self.email
