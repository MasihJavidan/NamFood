# Generated by Django 3.2.4 on 2021-07-22 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انشتار')),
                ('slug', models.SlugField(unique=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انشتار'), verbose_name='عنوان لاتین')),
            ],
        ),
    ]
