# Generated by Django 2.2.5 on 2019-10-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_auto_20191004_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_d',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
