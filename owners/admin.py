from django.contrib import admin
from owners.models import PetOwner


class PetOwnerDisplay(admin.ModelAdmin):
    list_display = ('writer','title','content','charge','species','is_reserved','photo','reservation_start','reservation_end','created_at','updated_at')
    fields =('writer','title','content','charge','species','is_reserved','photo','reservation_start','reservation_end','created_at','updated_at')
    readonly_fields = ('created_at','updated_at')
    
    
# Register your models here.
admin.site.register(PetOwner, PetOwnerDisplay)