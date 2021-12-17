from django.contrib import admin

from .models import Companions, Message


@admin.register(Companions)
class CompanionsAdmin(admin.ModelAdmin):
    search_fields = ('companion_id', )


@admin.register(Message)
class MesssageAdmin(admin.ModelAdmin):
    list_display = ('companion_id', 'msg_text', 'msg_time', )
    list_filter = ('companion_id', )
    search_fields = ('companion_id', )