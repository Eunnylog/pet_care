from rest_framework import serializers
from owners.models import PetOwner, PetOwnerComment


class PetOwner(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = "__all__"


class PetOwnerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwnerComment
        fields = "__all__"
        