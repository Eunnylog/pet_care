from rest_framework import serializers
from sitters.models import PetSitterComment, PetSitter
from owners.serializers import BaseSerializer


class PetSitterSerializer(BaseSerializer):
    writer = serializers.SerializerMethodField()
    is_reserved = serializers.SerializerMethodField()
    reservation_start = serializers.SerializerMethodField()
    reservation_end = serializers.SerializerMethodField()
    reservation_period = serializers.SerializerMethodField()
    
    
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
        model = PetSitter
        fields = "__all__"


class PetSitterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSitter
        fields = ("title","content", "charge","species","reservation_start", "reservation_end","location")


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
        