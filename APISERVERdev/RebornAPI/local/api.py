from .models import LocalLevel1, LocalLevel2, LocalLevel3, Place
from rest_framework import serializers, viewsets

class LocalLevel1Serializer(serializers.ModelSerializer):

    class Meta:
        model = LocalLevel1
        fields = '__all__'

class LocalLevel1ViewSet(viewsets.ModelViewSet):
    queryset = LocalLevel1.objects.all()
    serializer_class = LocalLevel1Serializer

class LocalLevel2Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = LocalLevel2
        fields = '__all__'

class LocalLevel2ViewSet(viewsets.ModelViewSet):
    queryset = LocalLevel2.objects.all()
    serializer_class = LocalLevel2Serializer

class LocalLevel3Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = LocalLevel3
        fields = '__all__'

class LocalLevel3ViewSet(viewsets.ModelViewSet):
    queryset = LocalLevel3.objects.all()
    serializer_class = LocalLevel3Serializer

class PlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Place
        fields = '__all__'

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer