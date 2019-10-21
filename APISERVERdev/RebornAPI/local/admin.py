from django.contrib import admin
from local.models import LocalLevel3, LocalLevel1, LocalLevel2, Place
# Register your models here.

admin.site.register(LocalLevel1)
admin.site.register(LocalLevel2)
admin.site.register(LocalLevel3)
admin.site.register(Place)
