# Generated by Django 4.2.6 on 2023-11-02 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_alter_post_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
    ]
