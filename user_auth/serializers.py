from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class BelongSerializer(serializers.ModelSerializer):

  class Meta:
    model = Belong
    fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Position
    fields = '__all__'


class SpeakerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Speaker
    fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

  speaker =SpeakerSerializer()
  class Meta:
    model = User
    fields = '__all__'


