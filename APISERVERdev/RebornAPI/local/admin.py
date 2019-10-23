from django.contrib import admin
from local.models import SpecialSi, Do, Si, Gu, Dong, Place
# Register your models here.


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(SpecialSi)
admin.site.register(Do)
admin.site.register(Si)
admin.site.register(Gu)
admin.site.register(Dong)
admin.site.register(Place, PlaceAdmin)
