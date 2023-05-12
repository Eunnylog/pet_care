from django.contrib import admin
from users.admin import CommonDisplayAdmin
from owners.models import PetOwner, PetOwnerComment


class PetOwnerDisplay(CommonDisplayAdmin):
    list_display = ('writer','title','content','charge','species','is_reserved','photo','reservation_start','reservation_end','reservation_period','location')
    fields =('writer','title','content','charge','species','is_reserved','photo','reservation_start','reservation_end','reservation_period','location')
    readonly_fields = ('reservation_period',)
    

class PetOwnerCommentDisplay(CommonDisplayAdmin):
    list_display = ('writer','owner_post','content')
    fields =('writer','owner_post','content')


admin.site.register(PetOwner, PetOwnerDisplay)
admin.site.register(PetOwnerComment, PetOwnerCommentDisplay)
