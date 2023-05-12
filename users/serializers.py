from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User, CheckEmail, PetOwnerReview, PetSitterReview
from django.db.models import Avg
from owners.serializers import PetOwnerSerializer
from sitters.serializers import PetSitterSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    def update(self,instance, validated_data):
        user = super().update(instance,validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("nick_name","photo",)

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    def update(self,instance, validated_data):
        user = super().update(instance,validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
class UserUpdatePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("nick_name","password","photo",)

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    def update(self,instance, validated_data):
        user = super().update(instance,validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

class UserDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("is_active",)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token["nick_name"] = user.nick_name
        return token


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

class MyPageSerializer(serializers.ModelSerializer):
    star_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    ownerreviews = PetOwnerReviewSerializer(many= True)
    sitterreviews = PetSitterReviewSerializer(many=True)
    petowner_set = PetOwnerSerializer(many=True)
    petsitter_set = PetSitterSerializer(many = True)

    def get_star_rating(self, obj):
        avg = obj.ownerreviews.aggregate(Avg('star'))
        return avg['star__avg']
    
    def get_review_count(self, obj):
        return obj.ownerreviews.count()

    class Meta:
        model=User
        fields = ('id','username','nick_name','star_rating','review_count','ownerreviews','sitterreviews','petowner_set','petsitter_set')