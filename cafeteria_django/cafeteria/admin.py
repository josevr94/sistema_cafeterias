from django.contrib import admin
from .models import Menu, Barista, Cafe, Resena, Proveedor

class MenuAdmin(admin.ModelAdmin):
    list_display=('id','nombre','descripcion','precio','categoria','imagen')
    search_fields = ('name',)
    
class BaristaAdmin(admin.ModelAdmin):
    pass

class CafeAdmin(admin.ModelAdmin):
    pass

class ResenaAdmin(admin.ModelAdmin):
    pass

class ProveedorAdmin(admin.ModelAdmin):
    pass



admin.site.register(Menu, MenuAdmin) 
admin.site.register(Barista, BaristaAdmin)
admin.site.register(Cafe, CafeAdmin)
admin.site.register(Resena,ResenaAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
# Register your models here.
