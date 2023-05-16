from rest_framework import serializers
from sitters.models import PetSitterComment, PetSitter
from owners.serializers import BaseSerializer
from users.models import PetSitterReview


class PetSitterReviewSerializer(BaseSerializer):
    writer = serializers.SerializerMethodField()
    sitter = serializers.SerializerMethodField()

    def get_writer(self, obj):
        return obj.writer.username
        
    def get_sitter(self, obj):
        return obj.sitter.username
    
    class Meta:
        model = PetSitterReview
        fields = '__all__'


class PetSitterSerializer(BaseSerializer):
    writer = serializers.SerializerMethodField()
    sitterreviews = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_reviews_count(self,obj):
        return obj.writer.sitterreviews.filter(show_status='1').count()
    
    def get_comments_count(self,obj):
        return obj.petsittercomment_set.filter(show_status='1').count()

    def get_sitterreviews(self, obj):
        serializer = PetSitterReviewSerializer(obj.writer.sitterreviews, many=True)
        return serializer.data
    
    def get_writer(self, obj):
        return obj.writer.username
    
    class Meta:
        model = PetSitter
        fields = ('writer','location','species','title','content','charge','photo','created_at','id','show_status','updated_at','sitterreviews','reviews_count','comments_count')


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
        