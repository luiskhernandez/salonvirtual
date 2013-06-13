from django.contrib import admin
from models import Presentacion, Diapositivas

class DiapositivasInline(admin.StackedInline):
    model = Diapositivas
class PresentacionAdmin(admin.ModelAdmin):
    inlines = [DiapositivasInline]

admin.site.register(Presentacion,PresentacionAdmin)    

