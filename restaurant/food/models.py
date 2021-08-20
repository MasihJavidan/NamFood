from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields import SlugField
from django.utils.translation import gettext as _
from django.utils import timezone

# Create your models here.
class Food(models.Model):
    FOOD_LIST = [
        ('drinks' , 'نوشیدنی ها'),
        ('breakfast' , 'صبحانه'),
        ('dinner' , 'شام'),
    ]
    
    STATUS = [
        ('draft' , 'Draft'),
        ('published' , 'Published'),
    ]

    name = CharField(_('نام غذا'), max_length=170)
    slug = SlugField(max_length=170, default='slug', unique_for_date='pub_time')
    description = models.TextField(_('توضیحات'))
    rate = models.IntegerField(_('امتیاز'), default=0,)
    price = models.IntegerField(_('قیمت براساس تومان'))
    time = models.IntegerField(_("زمان لازم"))
    pub_time = models.DateField(_("تاریخ انتشار"), default=timezone.now)
    photo = ImageField(upload_to='food/')
    type_food = CharField(_('نوع غدا'), max_length=10, choices= FOOD_LIST, default='dinner')
    status = CharField(max_length=10, choices=STATUS, default='draft')

    def __str__(self):
        return self.name
