# Generated by Django 3.2.4 on 2021-06-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20210614_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='type_food',
            field=models.CharField(default='Lunch', max_length=10, verbose_name='نوع غدا'),
        ),
    ]
