from django.shortcuts import render
from .models import Level1, Level2, Level3, Place, Filecheck, TrashInfo
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PlaceSerializer

from .serializers import PlaceSerializer, TrashInfoSerializer
import os, sys, glob, json
from PIL import Image
import datetime

from django.db.models import Q

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

@api_view(['POST'])
def plusTrash(request, place_pk):
    place = Place.objects.get(id=place_pk)
    print(place, '선택완료!')

    trash = request.POST['trash_num']

    if trash=='1':
        place.can += 1
    elif trash=='2':
        place.paper += 1
    elif trash=='3':
        place.plastic += 1
    else:
        place.mix += 1
    place.trashCount += 1
    place.save()
    serializer = PlaceSerializer(place)
    print(serializer.data)
    return Response(data=serializer.data)

@api_view(['GET'])
def filechecks(request):
    checkpoint = Filecheck.objects.get(pk=1)
    # print(datetime.datetime.now().strftime('%Y%m%d_%H:%M:%S'))
    return Response(data=checkpoint.count)

@api_view(['GET', 'POST'])
def trashinfo(request):
    ## 쓰레기 정보를 저장하는 모델 TrashInfo 와 관련된 함수입니다.

    # POST 요청으로 오는 경우는 쓰레기 이미지 결과값을 저장할 때 사용됩니다.

    # GET 요청으로 들어오는 경우는, 관리자가 실행할 수 있는 것이며,
    # 크게 아래와 같은 활동으로 이루어집니다.
    # 1. TrashInfo 에 있는 정보들을 json 파일 형식(현재 시간값을 파일 이름에 추가함으로써 유일성 보장)으로 저장
    # 2. Filecheck point update (나중에 새로 이미지 만들때, 이름의 유일성을 가지기 위함)
    # 3. input에 있는 파일(그림)들을 특정 디렉토리로 옮기기(ex, copy라는 폴더)
    # 4. Trashinfo에 저장되어 있던 image DB 내용 삭제

    if request.method == 'POST':
        trash_num = request.POST.get('trash_num')
        confused = request.POST.get('confused')
        
        if trash_num=='1':
            TrashInfo.objects.create(info='can', confused=confused)
        elif trash_num=='2':
            TrashInfo.objects.create(info='paper', confused=confused)
        elif trash_num=='3':
            TrashInfo.objects.create(info='plastic', confused=confused)
        else:
            TrashInfo.objects.create(info='mix', confused=confused)
            
        
        return Response(data=[])
    
    else:
        ## save trash related information!!
        # 1. save Trashinfo data > .json
        # 2. save next_num (using in .jpg name!)
        # 3. copy image (input > copy) and delete input image
        # 4. delete trashinfo data in model
        
        # 1
        
        # filter mixggggggggggggg
        confused_dic = TrashInfo.objects.filter(Q(confused=True) | Q(info='mix'))
        serializer = TrashInfoSerializer(confused_dic, many=True)
        with open(f'trashinfo_{datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S")}.json', 'w', encoding="utf-8") as make_file:
            json.dump(serializer.data, make_file, indent="\t\t")

        # 2
        input_dir = glob.glob("./local/input/*")
        input_files = [file for file in input_dir]
        input_ids = [int(name[14:].replace('.jpg', '')) for name in input_dir]
        checkpoint = Filecheck.objects.get(pk=1)
        checkpoint.count = TrashInfo.objects.latest('id').id
        checkpoint.save()
        print(input_files)
        print(input_ids)

        # 3
        for file in input_files:
            image = Image.open(file)
            copy_image = file.replace('input', 'copy')
            image.save(f'{copy_image}')
            os.remove(file)

        # 4
        TrashInfo.objects.all().delete()
        # for id in input_ids:
        #     image = TrashInfo.objects.get(pk=id)
        #     image.delete()

        return Response(data=serializer.data)
    
@api_view(['POST'])
def placeUpdate(request):
    place_pk = 1
    place = Place.objects.get(pk=place_pk)
    # how to alert to vue..?? arduino > python camera > views > vue????
    place.isFullMix = request.POST['full']
    # print(place.__dict__)
    place.save()
    
    return Response(data=[])
