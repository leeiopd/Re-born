<<<<<<< HEAD
from rest_framework import serializers
from .models import Place
=======
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Place, TrashInfo



>>>>>>> APISERVERdev

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
<<<<<<< HEAD
        fields = '__all__'
=======
        fields =  "__all__"

class TrashInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashInfo
        fields =  "__all__"
>>>>>>> APISERVERdev
