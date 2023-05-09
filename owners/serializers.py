from rest_framework import serializers
from owners.models import PetOwner, PetOwnerComment


class PetOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = "__all__"
        
        
class PetOwnerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ("title","content", "charge","species","reservation_start", "reservation_end")


class PetOwnerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwnerComment
        fields = "__all__"
        