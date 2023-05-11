from django.contrib import admin
from users.admin import CommonDisplayAdmin
from owners.models import PetOwner, PetOwnerComment


class PetOwnerDisplay(admin.ModelAdmin):
    list_display = ('writer','title','content','charge','species','is_reserved','photo','reservation_start','reservation_end','created_at','updated_at',"show_status",'reservation_period')
    fields =('writer','title','content','charge','species','is_reserved','photo','reservation_start','reservation_end','created_at','updated_at',"show_status",'reservation_period')
    readonly_fields = ('created_at','updated_at','reservation_period')
    

class PetOwnerCommentDisplay(CommonDisplayAdmin):
    list_display = ('writer','owner_post','content')
    fields =('writer','owner_post','content')


admin.site.register(PetOwner, PetOwnerDisplay)
admin.site.register(PetOwnerComment, PetOwnerCommentDisplay)
