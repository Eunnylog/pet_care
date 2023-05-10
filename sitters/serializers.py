from rest_framework import serializers
from sitters.models import PetSitterComment, PetSitter


class PetSitterSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField()
    
    def get_writer(self, obj):
        return obj.writer.username

    class Meta:
        model = PetSitter
        fields = "__all__"

class PetSitterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSitter
        fields = ("title","content", "charge","species","reservation_start", "reservation_end")


class PetSitterCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSitterComment
        fields = "__all__"
