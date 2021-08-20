# Generated by Django 3.2.4 on 2021-06-25 13:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_alter_food_pub_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='status',
            field=models.CharField(choices=[{'draft', 'Draft'}, ('published', 'Published')], default='draft', max_length=10),
        ),
        migrations.AlterField(
            model_name='food',
            name='pub_time',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار'),
        ),
    ]