from django.db import models

class PetOwnerReview(models.Model):
    comment = models.TextField()
    star = models.IntegerField()

class PetSitterReview(models.Model):
    comment = models.TextField()
    star = models.IntegerField()