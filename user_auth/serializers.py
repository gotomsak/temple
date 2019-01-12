from rest_framework import serializers
from django.contrib.auth.models import *

from .models import *


class RegionGroupSerializer(serializers.ModelSerializer):

  class Meta:
    model = RegionGroup
    fields = '__all__'


class LandGroupSerializer(serializers.ModelSerializer):

  class Meta:
    model = LandGroup
    fields = '__all__'


class GenerationGroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = GenerationGroup
    fields = '__all__'


class SpeakerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Speaker
    fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

  speaker = SpeakerSerializer()
  class Meta:
    model = User
    fields = '__all__'


