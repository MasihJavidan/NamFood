# Generated by Django 3.2.4 on 2021-07-28 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='عنوان لاتین'),
        ),
    ]