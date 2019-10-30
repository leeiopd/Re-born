from django.contrib.auth.models import User
from .models import Place, TrashInfo
from rest_framework import serializers


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields =  "__all__"

class TrashInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashInfo
        fields =  "__all__"
        # fields = ('id', 'username')
