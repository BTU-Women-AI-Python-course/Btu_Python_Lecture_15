from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    order = models.PositiveSmallIntegerField(verbose_name=_('Order'))

    def __str__(self):
        return f'Category name {self.title}, order: {self.order}'

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['order']
