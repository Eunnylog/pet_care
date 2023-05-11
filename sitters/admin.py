from django.contrib import admin
from users.admin import CommonDisplayAdmin
from sitters.models import PetSitter, PetSitterComment


class PetSitterDisplay(CommonDisplayAdmin):
    list_display = ('writer','title','content','charge','species','is_reserved','photo','reservation_start','reservation_end','reservation_period','location')
    fields = ('writer','title','content','charge','species','is_reserved','photo','reservation_start','reservation_end','reservation_period','location')
    readonly_fields = ('reservation_period',)


class PetSitterCommentDisplay(CommonDisplayAdmin):
    list_display = ('writer','sitter_post','content')
    fields =('writer','sitter_post','content')


admin.site.register(PetSitter, PetSitterDisplay)
admin.site.register(PetSitterComment, PetSitterCommentDisplay)
