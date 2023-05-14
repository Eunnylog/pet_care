from datetime import timedelta
from django.db import models
from django.utils import timezone
from users.models import User, CommonModel
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from django.urls import reverse


class Location(models.Model):
    class Meta:
        db_table = "location"

    city = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=20, default='')


class Species(models.Model):
    class Meta:
        db_table = "species_breeds"

    species = models.CharField(max_length=20, default='')
    breeds = models.CharField(max_length=30, default='')


class PetOwner(CommonModel):
    reservation_status = (
        ("0","미완료"),
        ("1","예약중"),
        ("2","완료"),
    )
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField("지역", max_length=50)
    species = models.CharField("종/품종", max_length=30)
    title = models.CharField("제목", max_length=20)
    content = models.TextField("내용")
    charge = models.PositiveIntegerField("요금")
    is_reserved = models.CharField("진행상태", max_length=20, choices=reservation_status, default="0") # 기본값을 0으로 주겠습니다
    photo = models.ImageField("이미지", blank=True)
    reservation_start = models.DateTimeField("예약시작일")
    reservation_end = models.DateTimeField("예약종료일")
    reservation_period = models.DurationField("예약기간")
    
    
    def __str__(self):
        return str(self.title)
    
    # 예약시작일과 현재날짜 비교
    # 예약 기간
    def save(self, **kwargs):
        if self.reservation_start < timezone.now():
          raise ValidationError("예약시작일이 오늘보다 이전일 수 없습니다.")
        if self.reservation_end < self.reservation_start:
            raise ValidationError('예약 종료일이 예약 시작일보다 이전일 수 없습니다.')
        else:    
            self.reservation_period = (self.reservation_end - self.reservation_start)
            super(CommonModel, self).save(**kwargs) # super의 첫번째 인자로 클래스명 , 객체 인스턴스가 들어갑니다

    def get_absolute_url(self):
        return reverse('petowner_detail_View', kwargs={'owner_id':self.pk})

class PetOwnerComment(CommonModel):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_post = models.ForeignKey(PetOwner, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.content)
    
    def get_absolute_url(self):
        return reverse('petowner_comment_view', kwargs={'owner_id': self.owner_post.pk})
    
    def get_detail_absolute_url(self):
        return reverse('petowner_comment_detail_view', kwargs={'owner_id': self.owner_post.pk, 'comment_id':self.pk})

class SittersForOwnerPR(CommonModel):
    owner_post = models.ForeignKey(PetOwner, on_delete=models.CASCADE)
    sitter = models.ForeignKey(User, on_delete=models.CASCADE)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return str(self.sitter)
    
    def get_absolute_url(self):
        return reverse('sittersforownerpr_view', kwargs={'owner_id': self.owner_post.pk})