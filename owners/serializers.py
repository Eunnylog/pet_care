from rest_framework import serializers
from owners.models import OwnerComment, PetOwner


class PetOwner(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = "__all__"

class OwnerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerComment
        fields = "__all__"