from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Contact(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length=50)
    email = models.EmailField(_("ایمیل"), max_length=254)
    message = models.TextField(_("متن"))

    def __str__(self):
        return self.name

    