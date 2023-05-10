from rest_framework import serializers
from users.models import PetOwnerReview, PetSitterReview

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