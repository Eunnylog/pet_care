from django.contrib import admin
from sitters.models import PetSitter, PetSitterComment


class PetSitterReviewDisplay(admin.ModelAdmin):
    list_display = ('writer','sitter','comment','star','created_at','updated_at',"show_status")
    fields =('writer','sitter','comment','star','created_at','updated_at',"show_status")
    readonly_fields = ('created_at','updated_at')


class PetSitterCommentDisplay(admin.ModelAdmin):
    list_display = ('writer','sitter_post','content','created_at','updated_at',"show_status")
    fields =('writer','sitter_post','content','created_at','updated_at',"show_status")
    readonly_fields = ('created_at','updated_at')


admin.site.register(PetSitter)
admin.site.register(PetSitterComment, PetSitterCommentDisplay)

