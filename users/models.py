from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator

class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    show_statuses=(('1','active'),
             ('2','hide'),
             ('3','delete'),)
    c=models.CharField(choices=show_statuses, max_length=1,default="1")
class UserManager(BaseUserManager):
    def create_user(self, username,email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username=models.CharField(max_length=50,unique=True)
    nick_name=models.CharField(max_length=50,default=True,null=True,blank=True)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




class PetOwnerReview(CommonModel):
    writer = models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'ownerreviews')
    content = models.TextField()
    star = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])

class PetSitterReview(CommonModel):
    writer = models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1)
    sitter = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'sitterreviews')
    content = models.TextField()
    star = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])