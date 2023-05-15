from datetime import timedelta
from django.utils import timezone
from django.db import models
from users.models import User, CommonModel
from django.core.exceptions import ValidationError
from owners.models import Location, Species


class PetSitter(CommonModel):
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30) #제목
    content = models.TextField() # 내용
    charge = models.PositiveIntegerField() # 요금
    location = models.CharField("지역", max_length=50)
    species = models.CharField("종/품종", max_length=30)
    photo = models.ImageField(blank=True) # 이미지

    def __str__(self):
        return self.title



class PetSitterComment(CommonModel):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    sitter_post = models.ForeignKey(PetSitter, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.content)
