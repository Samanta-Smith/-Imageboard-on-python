# Generated by Django 2.2.5 on 2019-10-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_auto_20191004_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_d',
            field=models.ImageField(upload_to=''),
        ),
    ]
