# Generated by Django 4.2.6 on 2023-11-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0015_alter_post_picture_alter_post_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='release_date',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
