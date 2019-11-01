# %config InlineBackend.figure_format = 'retina'

import serial
import matplotlib.pyplot as plt

import numpy as np
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models
import torchvision.transforms.functional as TF
from PIL import Image
from torch.autograd import Variable

from picamera import PiCamera

from time import sleep
import os, glob

import requests


def predict_image(image):
    image_tensor = test_transforms(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    input = Variable(image_tensor)
    input = input.to(device)
    output = model(input)
    # print(classes)
    #print(torch.exp(output))
    #max_percent = torch.max(torch.exp(output))
    tensors = sorted(torch.exp(output)[0])
    fourth, third, second, first = tensors
    
    confused = False

    if first >= 0.8:
        pass
    elif first >=0.6:
        if second * 3 > first:
            confused = True
    elif first >= 0.5:
        if second * 2.5 > first:
            confused = True
    else:
        confused = True
    
    if confused:
        index = 3
    else:
        index = output.data.cpu().numpy().argmax()
        
    return index, confused

## check trash and image classification and update DB!

# 1. find next_num using filechecks url to get next_num
# 2. Let's take a picture~~
# 3. Get deep learning model~
# 4. Get picture(capture before) and predict by using model
# 5. Go to result!!(by plt)
# 6. REQUESTS gogo~~
##

# 1. find next_num using filechecks url to get next_num
url_base = 'http://127.0.0.1:8080'
place_pk = 1
url_getnumber = '/api/filechecks/'
url_createtrashinfo = '/api/trashinfo/'
url_plus = f'/api/plustrash/{place_pk}/'
response = requests.get(url_base + url_getnumber)
next_num = response.json() + 1
# print(next_num, 'pppppppppppppppppppppppp')
# full_flag = False

ser = serial.Serial("/dev/ttyACM0", 9600)

before_flag = False
current_flag = False

while True:
    data = ser.readline()
    res = data.decode()
    

    if res == '5\r\n':
        # print('success')
        # camera start     
        current_flag = False
      
        # 2. Let's take a picture~~
        camera = PiCamera()
        camera.resolution = (450,450)
        #camera.start_preview()
        #sleep(5)
        camera.capture(f'./input/{next_num}.jpg')
        #camera.stop_preview()
        camera.close()

        # 3. Get deep learning model~
        device = torch.device('cpu')
        test_transforms = transforms.Compose([transforms.Resize(224),
                                              transforms.ToTensor(),
                                             ])
        model = torch.load('newModel3.pth', map_location=device)
        model.eval()
        classes = ['can', 'paper', 'plastic', 'trash']

        # 4. Get picture(capture before) and predict by using model
        image = Image.open(f'./input/{next_num}.jpg')
        index, confused = predict_image(image)
        print('predict : ', classes[index], ', confused? :' ,  confused)
        #print(type(index)) = <class 'numpy.int32'> , but it can be +1
        result = index + 1
        # print(result)

        # 5. Go to result!!
        # fig=plt.figure(figsize=(10,100))
        # sub = fig.add_subplot(4, 3, 1)
        # sub.set_title("▼ i'm predicted " + str(classes[index])+ ":)")
        # plt.axis('off')
        # plt.imshow(image)
        # plt.show()

        # print(classes[index[0]])
        
        # 6. REQUESTS (create trashinfo)
        # go to trashinfo model
        data = {'trash_num' : result , 'confused' : confused}
        response = requests.post(url_base + url_createtrashinfo, data=data)
        # print(response)

        # plus to location trash data
        data2 = {'trash_num' : result }
        response = requests.post(url_base + url_plus, data=data2)
        # print(response.__dict__)
        result = str(result)
        result = result.encode('utf-8')
        ser.write(result)
        # print('success~~~~~~~~~~~~~~~~~~~~~~~1')
        next_num += 1
      
    
    elif res == '1\r\n': # red(can) full
        current_flag = True
        # print('red is full')
        
    elif res == '2\r\n': # green(paper) full
        current_flag = True
        # print('green is full')
    
    elif res == '3\r\n': # plastic full
        current_flag = True
        # print('plastic is full')
        
    elif res == '4\r\n': # mix full
        current_flag = True
        # print('mix is full')
    
    if current_flag!=before_flag:
        url_tmp = '/api/placed/update/'
        data3 = {'full':current_flag}
        response = requests.post(url_base + url_tmp, data=data3)
        
        # if current_flag:
        #     print('lets axios >>> false > True')
        #     # change False > True
        # else:
        #     print('lets axios >>> true > False')
        
    before_flag = current_flag    
