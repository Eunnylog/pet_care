from rest_framework import serializers
from sitters.models import PetSitterComment


class PetSitterCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSitterComment
        fields = "__all__"
        