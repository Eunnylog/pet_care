from rest_framework import serializers
from owners.models import OwnerComment

class OwnerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerComment
        fields = "__all__"