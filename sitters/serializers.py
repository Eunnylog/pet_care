from rest_framework import serializers
from sitters.models import SitterComment

class SitterCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitterComment
        fields = "__all__"