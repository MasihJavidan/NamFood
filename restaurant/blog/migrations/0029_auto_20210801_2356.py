# Generated by Django 3.2.4 on 2021-08-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_alter_comments_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ('pub_time',)},
        ),
        migrations.AddField(
            model_name='comments',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='edit',
            field=models.DateTimeField(auto_now=True, verbose_name='ادیت'),
        ),
    ]
