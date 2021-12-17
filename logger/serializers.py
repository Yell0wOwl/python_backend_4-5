from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import *

User = get_user_model()

class CompanionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companions
        fields = '__all__'

    def validate_companion_name(self, name):
        if name.isalpha():
            return name
        else:
            raise serializers.ValidationError('Wrong name')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def validate_msg_time(self, time):
        if(int(time[:2])>23 or int(time[3:5])>59):
            raise serializers.ValidationError('Wrong time')
        else:
            return time
