from django.contrib import admin
from owners.models import PetOwner, PetOwnerComment

admin.site.register(PetOwner)
admin.site.register(PetOwnerComment)

class PetOwnerCommentDisplay(admin.ModelAdmin):
    list_display = ('writer','owner','content','created_at','updated_at')
    fields =('writer','owner','content','created_at','updated_at')
    readonly_fields = ('created_at','updated_at')
