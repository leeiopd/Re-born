from .models import Level1, Level2, Level3, Place
from rest_framework import serializers, viewsets

class Level1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Level1
        fields = '__all__'

class Level1ViewSet(viewsets.ModelViewSet):
    queryset = Level1.objects.all()
    serializer_class = Level1Serializer

class Level2Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Level2
        fields = '__all__'

class Level2ViewSet(viewsets.ModelViewSet):
    queryset = Level2.objects.all()
    serializer_class = Level2Serializer

class Level3Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Level3
        fields = '__all__'

class Level3ViewSet(viewsets.ModelViewSet):
    queryset = Level3.objects.all()
    serializer_class = Level3Serializer

class PlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Place
        fields = '__all__'

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer