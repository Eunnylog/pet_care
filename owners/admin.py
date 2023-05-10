from django.contrib import admin
from owners.models import PetOwner, PetOwnerComment


class PetOwnerDisplay(admin.ModelAdmin):
    list_display = ('writer','title','content','charge','species','is_reserved','photo','reservation_start','reservation_end','created_at','updated_at','reservation_period')
    fields =('writer','title','content','charge','species','is_reserved','photo','reservation_start','reservation_end','created_at','updated_at','reservation_period')
    readonly_fields = ('created_at','updated_at')
    

class PetOwnerCommentDisplay(admin.ModelAdmin):
    list_display = ('writer','owner_post','content','created_at','updated_at')
    fields =('writer','owner_post','content','created_at','updated_at')
    readonly_fields = ('created_at','updated_at')


admin.site.register(PetOwner, PetOwnerDisplay)
admin.site.register(PetOwnerComment, PetOwnerCommentDisplay)
