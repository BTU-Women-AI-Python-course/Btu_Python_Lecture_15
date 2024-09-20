from django.db import models
from django.utils.translation import gettext_lazy as _



class Attribute(models.Model):
    product = models.ForeignKey(
        to='product.Product',
        verbose_name=_("Product"),
        on_delete=models.CASCADE
    )
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=0)
    color = models.CharField(verbose_name=_('Color'), max_length=255)
    length = models.DecimalField(
        verbose_name=_('Length'),
        decimal_places=2,
        max_digits=6,
        blank=True, null=True
    )
    depth = models.DecimalField(
        verbose_name=_('Depth'),
        decimal_places=2,
        max_digits=6,
        blank=True, null=True
    )


    def __str__(self):
        return f'Attribute name {self.title}'

    class Meta:
        verbose_name = _('Attribute')
        verbose_name_plural = _('Attributes')
