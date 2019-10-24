from django.contrib import admin
from local.models import Level1, Level2, Level3, Place
# Register your models here.

class Level1Admin(admin.ModelAdmin):
    list_display = ['id', 'name']

class Level2Admin(admin.ModelAdmin):
    list_display = ['id', 'name']

class Level3Admin(admin.ModelAdmin):
    list_display = ['id', 'name']

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
admin.site.register(Level1, Level1Admin)
admin.site.register(Level2, Level2Admin)
admin.site.register(Level3, Level3Admin)
admin.site.register(Place, PlaceAdmin)
