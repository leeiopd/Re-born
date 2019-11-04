from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url('get-result/$', views.get_result, name='get_result'),
]
