from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    brand = models.ForeignKey(
        to='product.Brand',
        verbose_name=_("Brand"),
        on_delete=models.PROTECT,
        null=True
    )
    categories = models.ManyToManyField(
        to='product.Category',
        verbose_name=_("Categories"),
        blank=True
    )
    tags = models.ManyToManyField(
        to='product.Tag',
        verbose_name=_("Tags"),
        blank=True
    )
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True, null=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=5, decimal_places=2)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    create = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)

    def __str__(self):
        return f"Product name {self.title} - Price {self.price}"

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['-id']


    def get_price(self, quantity: int, discount: Decimal = Decimal(0)) -> Decimal:
        price = self.price * quantity
        price = (price * (100 - discount))/100
        return price

    @property
    def tag_titles(self):
        if not self.tags.exists():
            return ''
        tags = self.tags.values_list('title', flat=True)
        tag_titles = "Tag titles: "
        for tag in list(tags)[:-1]:
            tag_titles += f"{tag}, "
        tag_titles += f"{list(tags)[-1]}"
        return tag_titles
