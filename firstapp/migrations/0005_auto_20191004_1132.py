# Generated by Django 2.2.5 on 2019-10-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20191004_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name_d',
            field=models.TextField(max_length=20),
        ),
    ]