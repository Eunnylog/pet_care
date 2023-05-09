from rest_framework import serializers
from owners.models import PetOwnerComment


class PetOwnerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwnerComment
        fields = "__all__"
        