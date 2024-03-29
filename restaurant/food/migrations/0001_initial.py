# Generated by Django 3.2.4 on 2021-06-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('rate', models.ImageField(upload_to='', verbose_name='امتیاز')),
                ('price', models.IntegerField()),
                ('time', models.ImageField(upload_to='', verbose_name='زمان لازم')),
                ('pub_time', models.DateField(auto_now_add=True, verbose_name='تاریخ انتظار')),
                ('photo', models.ImageField(upload_to='food/')),
            ],
        ),
    ]
