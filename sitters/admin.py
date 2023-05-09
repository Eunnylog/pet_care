from django.contrib import admin
from sitters.models import PetSitter

class PetSitterReviewDisplay(admin.ModelAdmin):
    list_display = ('writer','sitter','comment','star','created_at','updated_at')
    fields =('writer','sitter','comment','star','created_at','updated_at')
    readonly_fields = ('created_at','updated_at')

# Register your models here.
admin.site.register(PetSitter)