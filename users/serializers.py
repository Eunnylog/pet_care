from rest_framework import serializers
from users.models import PetOwnerReview, PetSitterReview, User
from django.db.models import Avg

class PetOwnerReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwnerReview
        fields = ('content','star',)

class PetOwnerReviewSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField()

    def get_writer(self, obj):
        return obj.writer.username

    class Meta:
        model = PetOwnerReview
        fields = '__all__'

class PetSitterReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSitterReview
        fields = ('content','star',)

class PetSitterReviewSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField()

    def get_writer(self, obj):
        return obj.writer.username

    class Meta:
        model = PetSitterReview
        fields = '__all__'


class StarRatingSerializer(serializers.ModelSerializer):
    
    star_rating = serializers.SerializerMethodField()
    star_count = serializers.SerializerMethodField()

    def get_star_rating(self, obj):
        avg = obj.ownerreviews.aggregate(Avg('star'))
        return avg['star__avg']
    
    def get_star_count(self, obj):
        return obj.ownerreviews.count()
        
    class Meta:
        model = User
        fields = ('id','username','star_rating','star_count')