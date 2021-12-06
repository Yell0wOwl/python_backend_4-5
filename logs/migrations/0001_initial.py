# Generated by Django 3.2.9 on 2021-12-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('user_id', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True, verbose_name='Имя собеседника')),
                ('number', models.IntegerField(verbose_name='Количество сообщений')),
            ],
        ),
    ]