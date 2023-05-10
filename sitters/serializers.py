from rest_framework import serializers
from sitters.models import PetSitterComment, PetSitter


class PetSitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSitter
        fields = "__all__"

class PetSitterCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSitterComment
        fields = "__all__"
