from django.urls import path
from . import views

app_name = 'local'

urlpatterns = [
    path('lv2list/<int:level1_pk>/', views.lv2List, name="lv2List"),
    path('lv3list/<int:level2_pk>/', views.lv3List, name="lv3List"),
    path('placelist/<int:level3_pk>/', views.placeList, name="placeList"),
    # path('new/', views.new, name="new"),
]