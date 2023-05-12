from rest_framework import serializers
from owners.models import PetOwnerComment, PetOwner, SittersForOwnerPR


class PetOwnerSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField()
    
    def get_writer(self, obj):
        return obj.writer.username
    
    class Meta:
        model = PetOwner
        fields = "__all__"
        
        
class PetOwnerCreateSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')
    class Meta:
        model = PetOwner
        fields = ("title","content", "charge","species","reservation_start", "reservation_end","location", 'writer')

    
class PetOwnerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwnerComment
        fields = "__all__"


class PetOwnerCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwnerComment
        fields = ("content",)

class SittersForOwnerPRSerializer(serializers.ModelSerializer):
    # 아이디 값이 아닌 이름으로 표시
    # owner_post = serializers.StringRelatedField()
    # sitter = serializers.StringRelatedField()

    class Meta:
        model = SittersForOwnerPR
        fields = "__all__"
        