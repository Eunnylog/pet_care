from django.contrib import admin
from sitters.models import PetSitter, PetSitterComment


class PetSitterCommentDisplay(admin.ModelAdmin):
    list_display = ('writer','sitter','content','created_at','updated_at')
    fields =('writer','sitter','content','created_at','updated_at')
    readonly_fields = ('created_at','updated_at')

admin.site.register(PetSitter)
admin.site.register(PetSitterComment)
