# %config InlineBackend.figure_format = 'retina'

import matplotlib.pyplot as plt

import numpy as np
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models

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
    print(classes)
    print(torch.exp(output))
    max_percent = torch.max(torch.exp(output))
    if max_percent > 0.9):
        confused = False
    else:
        confused = True

    index = output.data.cpu().numpy().argmax()
    return index, confused

## this is ~~~~

# 1. check image amount in input_dir
# 2. Let's take a picture~~
# 3. Get deep learning model~
# 4. Get picture(capture before) and predict by using model
# 5. Go to result!!(by plt)
# 6. REQUESTS gogo~~
##


# 1. find next_num using filechecks url to get next_num
url_base = 'http://127.0.0.1:8000'
place_pk = 1
url_getnumber = '/api/filechecks/'
url_createtrashinfo = '/api/trashinfo/'
url_plus = f'/api/plustrash/{place_pk}/'
response = requests.get(url_base + url_getnumber)
next_num = response.json() + 1


# 2. Let's take a picture~~
camera = PiCamera()
camera.resolution = (450,450)
camera.start_preview()
sleep(5)
camera.capture(f'./input/{next_num}.jpg')
camera.stop_preview()


# 3. Get deep learning model~
device = torch.device('cpu')
test_transforms = transforms.Compose([transforms.Resize(224),
                                      transforms.ToTensor(),
                                     ])
model = torch.load('newModel3.pth', map_location=device)
model.eval()
classes = ['can', 'paper', 'plastic', 'trash']

import torchvision.transforms.functional as TF


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

data = {'trash_num' : result , 'confused' : confused}
response = requests.post(url_base + url_createtrashinfo, data=data)
print(response)

# if result=='1':
#     print('can')
# elif result=='2':
#     print('paper')
# elif result=='3':
#     print('plastic')
# else:
#     print('trash')
# #

data = {'trash_num' : result }
response = requests.post(url_base + url_plus, data=data)
# print(response.__dict__)
