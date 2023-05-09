from django.contrib import admin
from owners.models import PetSitter, PetSitterComment

admin.site.register(PetSitter)
admin.site.register(PetSitterComment)