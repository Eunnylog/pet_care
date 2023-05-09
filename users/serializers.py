from rest_framework import serializers
from users.models import PetOwnerReview, PetSitterReview
from users.models import User

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


class PetOwnerReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwnerReview
        fields = ('content','star',)

class PetOwnerReviewSerializer(serializers.ModelSerializer):
    petowner_set = serializers.SerializerMethodField()

    def get_petowner_set(self, obj):
        return obj.petowner_set.username

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