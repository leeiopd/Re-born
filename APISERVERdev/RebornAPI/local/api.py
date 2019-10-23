from .models import SpecialSi, Do, Si, Gu, Dong, Place
from rest_framework import serializers, viewsets

class SpecialSiSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialSi
        fields = '__all__'

class SpecialSiViewSet(viewsets.ModelViewSet):
    queryset = SpecialSi.objects.all()
    serializer_class = SpecialSiSerializer

class DoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Do
        fields = '__all__'

class DoViewSet(viewsets.ModelViewSet):
    queryset = Do.objects.all()
    serializer_class = DoSerializer

class SiSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Si
        fields = '__all__'

class SiViewSet(viewsets.ModelViewSet):
    queryset = Si.objects.all()
    serializer_class = SiSerializer

class GuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gu
        fields = '__all__'

class GuViewSet(viewsets.ModelViewSet):
    queryset = Gu.objects.all()
    serializer_class = GuSerializer

class DongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dong
        fields = '__all__'

class DongViewSet(viewsets.ModelViewSet):
    queryset = Dong.objects.all()
    serializer_class = DongSerializer

class PlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Place
        fields = '__all__'

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer