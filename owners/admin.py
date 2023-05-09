from django.contrib import admin
from owners.models import PetOwner, PetOwnerComment

admin.site.register(PetOwner)
admin.site.register(PetOwnerComment)