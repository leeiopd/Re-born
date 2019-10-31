from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Place, TrashInfo




class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields =  "__all__"

class TrashInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashInfo
        fields =  "__all__"