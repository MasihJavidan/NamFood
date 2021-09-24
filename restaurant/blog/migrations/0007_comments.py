# Generated by Django 3.2.4 on 2021-07-23 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام کاربری')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('content', models.CharField(max_length=500, verbose_name='متن')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='blog.post', verbose_name='دیدگاه')),
            ],
        ),
    ]