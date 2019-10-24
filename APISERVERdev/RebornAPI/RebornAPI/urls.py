"""RebornAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from django.contrib import admin
from django.urls import path
# from . import views

import local.api

app_name = 'local'

router = routers.DefaultRouter()
router.register('level1', local.api.Level1ViewSet)
router.register('level2', local.api.Level2ViewSet)
router.register('level3', local.api.Level3ViewSet)
router.register('place', local.api.PlaceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doc/', get_swagger_view(title='Rest API Document')),
    path('api/', include((router.urls, 'local'), namespace='api')),
    path('api/', include('local.urls')),
    # path('Si/', views.siList, name='si'),
]
