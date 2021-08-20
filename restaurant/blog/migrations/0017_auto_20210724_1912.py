# Generated by Django 3.2.4 on 2021-07-24 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(default=None, related_name='blogs', to='blog.Tag', verbose_name='تگ ها'),
        ),
    ]
