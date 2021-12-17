from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Companions(models.Model):
    companion_id = models.CharField(max_length=64, unique = True, verbose_name = 'ID собеседника', null = True)
    companion_name = models.CharField(max_length=64, verbose_name = 'Имя собеседника', null = True)

    def __str__(self):
        return self.companion_id

    class Meta:
        verbose_name_plural = 'Собеседники'
        ordering = ('companion_id',)

class Message(models.Model):
    user_id = models.CharField(max_length=64, verbose_name = 'ID пользователя', null = True)
    msg_text = models.CharField(max_length=64, verbose_name = 'Текст сообщения', null = True)
    msg_time = models.CharField(max_length=64, verbose_name = 'Время отправки', null = True)
    #companion_id = models.ForeignKey(Companions, on_delete = models.SET_NULL, verbose_name = 'ID собеседника', null = True)
    companion_id = models.CharField(max_length=64, verbose_name='ID собеседника', null=True)

    def __str__(self):
        return self.companion_id

    class Meta:
        verbose_name_plural = 'Сообщения'
        ordering = ('companion_id',)