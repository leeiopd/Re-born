from django.shortcuts import render
from rest_framework.decorators import api_view
import json
from ibm_watson import VisualRecognitionV3
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
import requests
from ibm_watson import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    version='2019-08-31',
    iam_apikey='f2a27751-55ca-4310-a229-4d433f6e2e33')
# from PIL import Image
# Create your views here.
# visual_recognition.disable_SSL_verification()
# from ibm_watson import DiscoveryV1
# # In the constructor
# visual_recognition = VisualRecognitionV3(version='2019-08-31', url='https://gateway.aibril-watson.kr/visual-recognition/api&version=2019-08-31',
#                                          username='c042db26-7bfb-4f0e-8229-05d82d71b1f6', password='HqSdojwRLrsH')


@api_view(['POST', 'GET'])
def get_result(request):
    if request.method == 'POST':
        path = request.data.get('src', None)
        result = {'data': path}
        print(result)
        # return Response(data=result, status=status.HTTP_200_OK)
        # image_file = Image.open(requests.get(path, stream=True).raw)

        response = requests.get(path, stream=True)
        response.raw.decode_content = True
        image_file = Image.open(response.raw)
        # image_file = Image.open(path)
        classes = visual_recognition.classify(
            url=path, images_filename=None, threshold='0.6', owners=["me"]).get_result()
        tmp = json.dumps(classes, indent=2)
        results = tmp.images.classifiers.classes
        print(results)
        val = 0
        for result in results:
            if result.score > val:
                val = result.score
                fin_val = result

        return Response(data=fin_val, status=status.HTTP_200_OK)
