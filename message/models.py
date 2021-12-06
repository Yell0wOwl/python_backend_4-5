from django.db import models
from logs.models import Log
# Create your models here.

class Message(models.Model):
    user_id = models.ForeignKey(Log, primary_key = True, on_delete = models.CASCADE, verbose_name = 'Имя собеседника')
    text = models.CharField(max_length=64, verbose_name = 'Текст сообщения')
