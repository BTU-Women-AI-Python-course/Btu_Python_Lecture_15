from django.db import models
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)


    def __str__(self):
        return f'Brand name {self.title}'

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')
