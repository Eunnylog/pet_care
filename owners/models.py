from django.db import models
from users.models import User


class PetOwner(models.Model):
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    charge = models.IntegerField()
    species_ = (
        ("cat", "고양이"),
        ("dog", "강아지"),
        ("Mammal",'포유류'),
        ("birds", "조류"),
        ("reptile", "파충류"),
        ("fish", "어류"),
        ("amphibian", "양서류"),
        ("rodents", "설치류"),
        ("etc", "기타"),
    )
    species = models.CharField("종", max_length=20, choices=species_)


class PetOwnerComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    PetOwner = models.ForeignKey(PetOwner, on_delete=models.CASCADE)
    # updated_at user에서 상속받아오기
    content = models.TextField()

    def __str__(self):
        return str(self.content)
