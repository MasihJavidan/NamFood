# Generated by Django 3.2.4 on 2021-07-22 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_auto_20210630_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.IntegerField(verbose_name='قیمت براساس تومان'),
        ),
    ]
