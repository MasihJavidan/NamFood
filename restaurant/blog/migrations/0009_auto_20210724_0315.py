# Generated by Django 3.2.4 on 2021-07-23 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comments_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post', verbose_name='دیدگاه'),
        ),
    ]