from django.contrib import admin
from users.admin import CommonDisplayAdmin
from sitters.models import PetSitter, PetSitterComment


class PetSitterDisplay(CommonDisplayAdmin):
    list_display = ('writer','title','content','charge','species','photo','location')
    fields = ('writer','title','content','charge','species','photo','location')


class PetSitterCommentDisplay(CommonDisplayAdmin):
    list_display = ('writer','sitter_post','content')
    fields =('writer','sitter_post','content')


admin.site.register(PetSitter, PetSitterDisplay)
admin.site.register(PetSitterComment, PetSitterCommentDisplay)
