from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}

class UserRoles(models.TextChoices):
    ADMIN = 'admin', _('administrator')
    MODERATOR = 'moderator', _('moderator')
    MEMBER = 'member', _('member')


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name=_('email address'), unique=True)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name=_('role'))
    first_name = models.CharField(max_length=30, verbose_name=_('first name'), **NULLABLE)
    last_name = models.CharField(max_length=30, verbose_name=_('last name'), **NULLABLE)
    phone_number = models.CharField(max_length=20, verbose_name=_('phone number'), **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['id', 'last_name', 'first_name']