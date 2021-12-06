from django.db import models

# Create your models here.

class Log(models.Model):
    user_id = models.CharField(max_length=64, primary_key = True, unique = True, verbose_name = 'Имя собеседника')
    number = models.IntegerField(verbose_name = 'Количество сообщений')

