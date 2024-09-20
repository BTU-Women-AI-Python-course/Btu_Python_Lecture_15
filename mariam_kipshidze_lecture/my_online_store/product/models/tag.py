from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    order = models.PositiveSmallIntegerField(verbose_name=_('Order'))

    def __str__(self):
        return f'Tag {self.title}'

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
        ordering = ['order']
