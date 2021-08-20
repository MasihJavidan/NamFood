from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):

    STATUS = (
        ('draft','Draft'),
        ('publish', 'Publish'),
    )

    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"), blank=True, null=True)
    description = models.CharField(_('توضیحات'), max_length=150)
    photo = models.ImageField(_("تصویر"), upload_to='blogs/', blank=True, null=True)
    content = RichTextField()
    pub_time = models.DateTimeField(_("زمان انتشار"), default=timezone.now)
    author = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    category = models.ForeignKey("Category", verbose_name=_("دسته بندی"), related_name='blog',on_delete=models.CASCADE, default=None)
    tags = models.ManyToManyField("Tag", verbose_name=_("تگ ها"), related_name='blogs', default=None)
    status = models.CharField(_('وضعیت'), max_length=10, choices=STATUS, default='draft')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    create_at = models.DateTimeField(_("تاریخ انشتار"), auto_now=False, auto_now_add=True)
    slug = models.SlugField(_("عنوان لاتین"), unique=create_at)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    pub_time = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(_("تاریخ بروزرسانی"), auto_now=True, auto_now_add=False)
 
    def __str__(self):
        return self.title


class Comments(models.Model):
    comments = models.ForeignKey('Post', verbose_name=_("مقاله"), related_name='comments', on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(_("نام کاربری"), max_length=100)
    email = models.EmailField(_("ایمیل"), max_length=254)
    content = models.TextField(_("متن"))
    pub_time = models.DateTimeField(_("زمان"), auto_now=False, auto_now_add=True)
    edit = models.DateTimeField(_('ادیت'), auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('pub_time',)

    def __str__(self):
        return self.name
