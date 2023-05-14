from rest_framework import serializers
from owners.models import PetOwnerComment, PetOwner, SittersForOwnerPR
from users.models import PetOwnerReview, User



class BaseSerializer(serializers.ModelSerializer):
    show_status = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    
    def get_show_status(self, obj):
        if obj.show_status == '1':
            return 'active'
        elif obj.show_status == '2':
            return 'hide'
        elif obj.show_status == '3':
            return 'delete'
    
    def get_created_at(self, obj):
        return obj.created_at.strftime("%Y년 %m월 %d일 %p %I:%M")
    
    def get_updated_at(self, obj):
        return obj.updated_at.strftime("%Y년 %m월 %d일 %p %I:%M")
    

class PetOwnerReviewSerializer(BaseSerializer):
    writer = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()

    def get_writer(self, obj):
        return obj.writer.username
    
    def get_owner(self, obj):
        return obj.owner.username

    class Meta:
        model = PetOwnerReview
        fields = '__all__'
        
        
class PetOwnerSerializer(BaseSerializer):
    writer = serializers.SerializerMethodField()
    is_reserved = serializers.SerializerMethodField()
    reservation_start = serializers.SerializerMethodField()
    reservation_end = serializers.SerializerMethodField()
    reservation_period = serializers.SerializerMethodField()
    ownerreviews = serializers.SerializerMethodField()

    def get_ownerreviews(self, obj):
        serializer = PetOwnerReviewSerializer(obj.writer.ownerreviews, many=True)
        return serializer.data

    
    def get_writer(self, obj):
        return obj.writer.username
    
    def get_is_reserved(self, obj):
        if obj.is_reserved == "0":
            return "미완료"
        elif obj.show_status == "1":
            return "예약중"
        elif obj.show_status == "2":
            return "완료"
    
    def get_reservation_start(self, obj):
        return obj.reservation_start.strftime("%Y년 %m월 %d일 %p %I:%M")

    def get_reservation_end(self, obj):
        return obj.reservation_end.strftime("%Y년 %m월 %d일 %p %I:%M")

    def get_reservation_period(self, obj):
        seconds = int(obj.reservation_period.total_seconds())
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return f"{days}일 {hours}시간 {minutes}분"

        
    class Meta:
        model = PetOwner
        fields = ('writer','location','species','title','content','charge','is_reserved','photo','reservation_start','reservation_end','reservation_period','created_at','id','show_status','updated_at','ownerreviews')
        
        
class PetOwnerCreateSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')
    class Meta:
        model = PetOwner
        fields = ("title","content", "charge","species","reservation_start", "reservation_end","location", "writer", "photo")

    
class PetOwnerCommentSerializer(BaseSerializer):
    writer = serializers.SerializerMethodField()
    owner_post = serializers.SerializerMethodField()
    
    def get_writer(self, obj):
        return obj.writer.username
    
    def get_owner_post(self, obj):
        return obj.owner_post.title
    
    class Meta:
        model = PetOwnerComment
        fields = ("writer", "owner_post", "content")


class PetOwnerCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwnerComment
        fields = ('content',)

class UserDetailSerializer(serializers.ModelSerializer):
    date_joined = serializers.SerializerMethodField()
    
    def get_date_joined(self, obj):
        return obj.date_joined.strftime("%Y년 %m월 %d일 %p %I:%M")
    
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password":{
                "write_only":True,
            },
            "is_admin":{
                "write_only":True,
            },
            "is_active":{
                "write_only":True,
            }
        }


class SittersForOwnerPRSerializer(BaseSerializer):
    owner_post = serializers.SerializerMethodField()
    sitter = UserDetailSerializer()
    
    def get_owner_post(self, obj):
        return obj.owner_post.title
    
    def get_sitter(self, obj):
        return obj.sitter.username
    
    class Meta:
        model = SittersForOwnerPR
        fields = "__all__"
        