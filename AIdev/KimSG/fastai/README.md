# Fastai 라이브러리 사용

Fastai 를 이용하여 이미지분류를 하였습니다. data 폴더에 있는 이미지, 모델을 이용하여 정확성을 구할 수 있습니다. 

- answer.ipynb : 모델 누적하기 위한 source code

- test.ipynb : 참고로 하였던 source code (참고만 하시고 실행은.. 코드 이해가 필요할 것입니다.)
- savefiles : test.ipynb에 필요한 자료들이며, 백업한 것입니다.



- 패키지 관리 시스템 : Anaconda
- 아래의 활동은 Anaconda 설치 이후에 가상환경 설정한 방법입니다.

```anaconda
conda version
# conda 4.7.10
```



## 목차

- 가상환경 생성 부터 학습된 딥러닝 모델을 통해 정확성 측정까지
  1. 가상환경 생성
  2. 필요한 package 설치
  3. 딥러닝 모델 만들기 ( python 코드 관련 )
  4. 딥러닝 모델을 통한 이미지 분류 정확성 확인하기
  5. 4에서 구한 결과값( 너가 보낸 이미지는 '~~'이다!!) 라즈베리로 보내기 ( 추후 예정 )
  6. 라즈베리에서 아두이노로 보내기 ( 추후 예정 )



### 1. 가상환경 생성 (이때 python 버전 설정도 함께)

- 생성

  ```anaconda
  conda create -n (가상환경이름) python=3.7
  ```

- 조회

  ```anaconda
  # 가상환경 list 조회
  conda info --envs
  
  # 특정 가상환경에 설치된 패키지 list 조회
  conda list
  ```

- 삭제

  ```anaconda
  conda env remove -n (가상환경이름)
  ```


- 가상환경 활성화

  ```anaconda
  conda activate (가상환경이름)
  ```

- 가상환경 비활성화

  ```anaconda
  conda deactivate
  ```

  

### 2. 필요한 package 설치

```anaconda
conda install -c conda-forge jupyterlab
conda install -c pytorch -c fastai fastai
conda install glob2
conda install scikit-learn
conda install seaborn
```



### 3. 딥러닝 모델 만들기 ( python 코드 관련 )

- 파일 설명
  - data : test, train, valid, models

    - models : 여기에 딥러닝 모델이 저장되고 불러올 수 있습니다.

  - 모델 만드는 법

    ```python
    ## 공통 필수 코드 : (1) 이라고 부르겠습니다.
    
    %reload_ext autoreload
    %autoreload 2
    %matplotlib inline
    
    %config InlineBackend.figure_format = 'retina'
    
    from fastai.vision import *
    from fastai.metrics import error_rate
    from pathlib import Path
    from glob2 import glob
    
    from sklearn.metrics import confusion_matrix
    
    import pandas as pd
    import numpy as np
    import os
    import zipfile as zf
    import shutil
    import re
    import seaborn as sns
    
    
    
    path = Path(os.getcwd())/"data"
    path
    
    tfms = get_transforms(do_flip=True,flip_vert=True)
    data = ImageDataBunch.from_folder(path,test="test",ds_tfms=tfms,bs=16)
    
    learn = create_cnn(data,models.resnet34,metrics=error_rate)
    
    learn.lr_find(start_lr=1e-6,end_lr=1e1)
    learn.recorder.plot()
    ```

    ```python
    answer = {}
    # xx 는 내가 학습시키고자 하는 train 횟수(정수)
    xx : 10 
         
    learn.fit_one_cycle(xx,max_lr=5.13e-03) 
    
    interp = ClassificationInterpretation.from_learner(learn) 
    losses,idxs = interp.top_losses()
    doc(interp.plot_top_losses)
    
    preds = learn.get_preds(ds_type=DatasetType.Test)
    max_idxs = np.asarray(np.argmax(preds[0],axis=1))
    yhat = []
    for max_idx in max_idxs:
        yhat.append(data.classes[max_idx])
    y = []
    
    ## convert POSIX paths to string first
    for label_path in data.test_ds.items:
        y.append(str(label_path))
    
    ## then extract waste type from file path
    pattern = re.compile("([a-z]+)[0-9]+")
    for i in range(len(y)):
        y[i] = pattern.search(y[i]).group(1)
    cm = confusion_matrix(y,yhat)
    print(cm)
    correct = 0
    
    for r in range(len(cm)):
        for c in range(len(cm)):
            if (r==c):
                correct += cm[r,c]
    accuracy = correct/sum(sum(cm))
    answer.update({xx:accuracy})
    
    learn.save(f'{xx}_cycle')
    ```

    

  - 모델 save, load하는 법

    ```python
    # save 방법 (ex, xx = 10)
    xx = 10
    learn.save(f'{xx}_cycle')
    ```

    ```python
    # load 방법 (ex, xx = 10)
    xx = 10
    learn1 = learn.load(f'{xx}_cycle')
    ```

    

### 4. 딥러닝 모델을 통한 이미지 분류 정확성 확인하기

```python
# (1) 를 여기에 복붙하시고~ 
xx = 10
learn1 = learn.load(f'{xx}_cycle')

preds = learn1.get_preds(ds_type=DatasetType.Test)
max_idxs = np.asarray(np.argmax(preds[0],axis=1))
yhat = []
for max_idx in max_idxs:
    yhat.append(data.classes[max_idx])
y = []

## convert POSIX paths to string first
for label_path in data.test_ds.items:
    y.append(str(label_path))

## then extract waste type from file path
pattern = re.compile("([a-z]+)[0-9]+")
for i in range(len(y)):
    y[i] = pattern.search(y[i]).group(1)
cm = confusion_matrix(y,yhat)
print(cm)
correct = 0

for r in range(len(cm)):
    for c in range(len(cm)):
        if (r==c):
            correct += cm[r,c]
accuracy = correct/sum(sum(cm))
print(accuracy)
# print(answer)
```



### 5. 결과를 라즈베리파이에서 확인 (추후 예정)

### 6. 결과를 아두이노로 전달하였는지 확인 (추후 예정)



### 참고 사이트

- https://nbviewer.jupyter.org/github/collindching/Waste-Sorter/blob/master/Waste%20sorter.ipynb
- https://github.com/collindching/Waste-Sorter/blob/master/Waste%20sorter.ipynb
- https://medium.com/@josh_2774/deep-learning-with-pytorch-9574e74d17ad



