from rest_framework import serializers
from owners.models import PetOwnerComment, PetOwner


class PetOwnerSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField()
    
    def get_writer(self, obj):
        return obj.writer.username
    
    class Meta:
        model = PetOwner
        fields = "__all__"
        
        
class PetOwnerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ("title","content", "charge","species","reservation_start", "reservation_end")

    
class OwnerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwnerComment
        fields = "__all__"


class PetOwnerCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwnerComment
        fields = ("content",)
