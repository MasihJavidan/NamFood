# Generated by Django 3.2.4 on 2021-07-24 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_comments_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.post', verbose_name='مقاله'),
        ),
    ]
