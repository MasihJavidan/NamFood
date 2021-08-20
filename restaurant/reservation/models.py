from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Reservation(models.Model):
    Number = [
        (1 , 1),
        (2 , 2),
        (3 , 3),
        (4 , 4),
        (5 , 5),
        (6 , 6),
        (7 , 7),
    ]
    name = models.CharField(_('نام و نام خانوادگی'), max_length=100)
    email = models.EmailField(_('پست الکترونیکی'))
    number = models.IntegerField(_('تعداد'), choices=Number, default=1)
    phone = models.CharField(_('تلفن'), max_length=20)
    date = models.DateField(_('تاریخ'))
    time = models.TimeField(_('ساعت'))

    def __srt__(self):
        return self.phone
