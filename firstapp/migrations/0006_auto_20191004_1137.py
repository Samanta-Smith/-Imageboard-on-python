# Generated by Django 2.2.5 on 2019-10-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20191004_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name_d',
            field=models.CharField(max_length=20),
        ),
    ]
