# Generated by Django 3.2.4 on 2021-07-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20210722_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='number',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], default=1, verbose_name='تعداد'),
        ),
    ]
