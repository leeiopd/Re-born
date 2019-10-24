from django.shortcuts import render
from .models import Level1, Level2, Level3, Place
from rest_framework.response import Response

# Create your views here.
def lv2List(request, level1_pk):
    level1 = Level1.objects.get(id=level1_pk)
    Level2s = level1.level2_set.all()
    # print(Level2s)
    result = []
    for Level2 in Level2s:
        print(Level2)
        result.append(Level2)
    print('출력완료')
    return Response(data=result)

def lv3List(request, level2_pk):
    level2 = Level2.objects.get(id=level2_pk)
    Level3s = level2.level3_set.all()
    result = []
    for Level3 in Level3s:
        print(Level3)
        result.append(Level3)
    print('출력완료')
    return Response(data=result)

def placeList(request, level3_pk):
    level3 = Level3.objects.get(id=level3_pk)
    Places = level3.place_set.all()
    result = []
    for Place in Places:
        print(Place)
        result.append(Place)
    print('출력완료')
    return Response(data=result)