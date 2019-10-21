from django.db import models

# Create your models here.
class LocalLevel1(models.Model): # 시, 도
    name = models.CharField(max_length=30)
    trashMixed = models.IntegerField()
    trashRecycled = models.IntegerField()

    def __str__(self):
        return self.name

class LocalLevel2(models.Model): # 구
    name = models.CharField(max_length=50)
    locallevel1 = models.ForeignKey(LocalLevel1, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class LocalLevel3(models.Model): # 동읍면리
    name = models.CharField(max_length=50)
    locallevel2 = models.ForeignKey(LocalLevel2, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Place(models.Model): # 설치된 지점 ex) 삼성연수원점
    name = models.CharField(max_length=50)
    locallevel3 = models.ForeignKey(LocalLevel3, on_delete=models.CASCADE)
    trashCount = models.IntegerField()
    mix = models.IntegerField()
    paper = models.IntegerField()
    plastic = models.IntegerField()
    can = models.IntegerField()

    def __str__(self):
        return self.name