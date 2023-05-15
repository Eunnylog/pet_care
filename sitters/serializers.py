from rest_framework import serializers
from sitters.models import PetSitterComment, PetSitter
from owners.serializers import BaseSerializer


class PetSitterSerializer(BaseSerializer):
    writer = serializers.SerializerMethodField()
    
    def get_writer(self, obj):
        return obj.writer.username
    
    class Meta:
        model = PetSitter
        fields = "__all__"


class PetSitterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSitter
        fields = ("title","content", "charge","species","location")


class PetSitterCommentSerializer(BaseSerializer):
    writer = serializers.SerializerMethodField()
    
    def get_writer(self, obj):
        return obj.writer.username
    
    
    class Meta:
        model = PetSitterComment
        fields = "__all__"


class PetSitterCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSitterComment
        fields = ("content",)
        