from django.shortcuts import render
from .models import Level1, Level2, Level3, Place
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def lv1List(request):
    Level1s = Level1.objects.all()
    result = []
    for level1 in Level1s:
        print(level1.name, level1.pk)
        tmp = {}
        tmp['pk'] = level1.pk
        tmp['name'] = level1.name
        result.append(tmp)
    print(result)
    print('출력완료')
    return Response(data=result)


@api_view(['GET'])
def lv2List(request, level1_pk):
    level1 = Level1.objects.get(id=level1_pk)
    Level2s = level1.level2_set.all()
    # print(Level2s)
    result = []
    for level2 in Level2s:
        print(level2.name, level2.pk)
        tmp = {}
        tmp['pk'] = level2.pk
        tmp['name'] = level2.name
        result.append(tmp)
    print(result)
    print('출력완료')
    return Response(data=result)

@api_view(['GET'])
def lv3List(request, level2_pk):
    level2 = Level2.objects.get(id=level2_pk)
    Level3s = level2.level3_set.all()
    result = []
    for level3 in Level3s:
        print(level3.name, level3.pk)
        tmp = {}
        tmp['pk'] = level3.pk
        tmp['name'] = level3.name
        result.append(tmp)
    print(result)        
    print('출력완료')
    return Response(data=result)

@api_view(['GET'])
def placeList(request, level3_pk):
    level3 = Level3.objects.get(id=level3_pk)
    Places = level3.place_set.all()
    result = []
    for place in Places:
        print(place.name, place.pk)
        tmp = {}
        tmp['pk'] = place.pk
        tmp['name'] = place.name
        result.append(tmp)
    print('출력완료')
    return Response(data=result)