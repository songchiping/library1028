# Generated by Django 4.2.6 on 2023-11-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.TextField(null=True),
        ),
    ]
