from django.contrib import admin
from users.admin import CommonDisplayAdmin
from sitters.models import PetSitter, PetSitterComment


# class PetSitterReviewDisplay(admin.ModelAdmin):
#     list_display = ('writer','sitter','comment','star','created_at','updated_at',"show_status")
#     fields =('writer','sitter','comment','star','created_at','updated_at',"show_status")
#     readonly_fields = ('created_at','updated_at')


class PetSitterCommentDisplay(CommonDisplayAdmin):
    list_display = ('writer','sitter_post','content')
    fields =('writer','sitter_post','content')


# admin.site.register(PetSitter)
admin.site.register(PetSitterComment, PetSitterCommentDisplay)
