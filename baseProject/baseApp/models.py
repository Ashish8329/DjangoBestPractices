from django.db import models
from django.utils.translation import gettext_lazy as _

from base.base_models import BaseModel


class User(BaseModel):
    username = models.CharField(
        max_length=100,
        verbose_name=_("Username"),
        null=True,  # db nullability
        blank=True,  # allow null values
        help_text=_("This is the user's name."),
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username if self.username else "Unnamed User"
