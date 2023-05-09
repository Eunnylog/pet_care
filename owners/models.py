from datetime import timedelta
from django.db import models
from users.models import User, CommonModel
from django.core.exceptions import ValidationError


class PetOwner(CommonModel):
    species_ = (
        ("cat", "고양이"),
        ("dog", "강아지"),
        ("mammal",'포유류'),
        ("birds", "조류"),
        ("reptile", "파충류"),
        ("fish", "어류"),
        ("amphibian", "양서류"),
        ("rodents", "설치류"),
        ("etc", "기타"),
    )
    reservation_status = (
        ("0","미완료"),
        ("1","예약중"),
        ("2","완료"),
    )
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("제목",max_length=20)
    content = models.TextField("내용")
    charge = models.PositiveIntegerField("요금")
    species = models.CharField("종", max_length=20, choices=species_)
    is_reserved = models.CharField("진행상태", max_length=20, choices=reservation_status, default="0") # 기본값을 0으로 주겠습니다
    photo = models.ImageField("이미지", blank=True)
    reservation_start = models.DateField("예약시작일")
    reservation_end = models.DateField("예약종료일")
    reservation_period = models.DurationField("예약기간")
    
    
    def __str__(self):
        return str(self.title)
    
    # 예약 기간
    def save(self, **kwargs):
        if self.reservation_end < self.reservation_start:
            raise ValidationError('예약 종료일이 예약 시작일보다 이전일 수 없습니다.')
        else:    
            self.reservation_period = (self.reservation_end - self.reservation_start) + timedelta(days=1)
            super(PetOwner, self).save(**kwargs) # super의 첫번째 인자로 클래스명 , 객체 인스턴스가 들어갑니다




class PetOwnerComment(CommonModel):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_post = models.ForeignKey(PetOwner, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.content)
