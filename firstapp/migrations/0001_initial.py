# Generated by Django 2.2.5 on 2019-10-02 09:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_d', models.CharField(max_length=20)),
                ('image_d', models.ImageField(upload_to='')),
                ('text_d', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('last_pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_d', models.ImageField(upload_to='')),
                ('text_d', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='firstapp.Post', verbose_name='Пост')),
            ],
        ),
    ]
