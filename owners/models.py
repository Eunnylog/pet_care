from django.db import models
from users.models import User, CommonModel


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
    charge = models.IntegerField("요금")
    species = models.CharField("종", max_length=20, choices=species_)
    is_reserved = models.CharField("진행상태", max_length=20, choices=reservation_status, default="0") # 기본값을 0으로 주겠습니다
    photo = models.ImageField("이미지", blank=True)
    reservation_start = models.DateField("예약시작일")
    reservation_end = models.DateField("예약종료일")
    # reservation_data = models.DurationField("예약기간") # 있어야하나?
    
    
    def __str__(self):
        return str(self.title)
    
    # 예약 기간
    def reservation(self):
        return self.reservation_end - self.reservation_start




class PetOwnerComment(CommonModel):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_post = models.ForeignKey(PetOwner, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.content)
