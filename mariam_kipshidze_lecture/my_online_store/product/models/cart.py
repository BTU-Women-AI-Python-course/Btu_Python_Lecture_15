from django.db import models
from django.utils.translation import gettext_lazy as _



class Cart(models.Model):
    user = models.OneToOneField(
        to='auth.User',
        verbose_name=_('User'),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'User {self.user.first_name} cart'

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')
