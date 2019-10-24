from django.db import models

# Create your models here.
class Level1(models.Model): # 특별시, 광역시, 도
    name = models.CharField(max_length=30)
    trashMixed = models.IntegerField()
    trashRecycled = models.IntegerField()

    def __str__(self):
        return self.name

class Level2(models.Model): # xx시 xx구 or xx구
    name = models.CharField(max_length=30)
    level1 = models.ForeignKey(Level1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Level3(models.Model): # 시
    name = models.CharField(max_length=50)
    level2 = models.ForeignKey(Level2, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Place(models.Model): # 설치된 지점 ex) 삼성연수원점
    name = models.CharField(max_length=50)
    level3 = models.ForeignKey(Level3, on_delete=models.CASCADE)
    trashCount = models.IntegerField()
    mix = models.IntegerField()
    paper = models.IntegerField()
    plastic = models.IntegerField()
    can = models.IntegerField()
    isFullPaper = models.BooleanField(default=False)
    isFullCan = models.BooleanField(default=False)
    isFullPlastic = models.BooleanField(default=False)
    isFullMix = models.BooleanField(default=False)    

    def __str__(self):
        return self.name

# class Gu(models.Model): # 구
#     name = models.CharField(max_length=50)
#     si = models.ForeignKey(Si, on_delete=models.CASCADE, blank = True, null = True)
#     specialsi = models.ForeignKey(SpecialSi, on_delete=models.CASCADE, blank = True, null = True)

#     def __str__(self):
#         return self.name

# class Dong(models.Model): # 동읍면리
#     name = models.CharField(max_length=50)
#     gu = models.ForeignKey(Gu, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.name