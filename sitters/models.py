from django.db import models
from users.models import User

class PetSitter(models.Model):
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20) #제목
    content = models.TextField(null=True) # 내용
    # location = models.PointField(blank=False, null=False) # 지역
    charge = models.PositiveIntegerField() # 요금
    species = (
        ('dog', '강아지'),
        ('cat', '고양이'),
        ('mammal', '포유류'),
        ('bird', '조류'),
        ('reptile', '파충류'),
        ('fish', '어류'),
        ('amphibian', '양서류'),
        ('rodents', '설치류'),
        ('etc', '기타'),
    )
    # species = models.Choices(choices=species) # 종
    # photo = models.ImageField(null=True) # 이미지


    def __str__(self):
        return self.title


class SitterComment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # pr? = models.ForeignKey(PR?, on_delete=models.CASCADE)
    # updated_at 처리는 어떻게?
    content = models.TextField()

    def __str__(self):
        return str(self.content)

# 안녕하세요