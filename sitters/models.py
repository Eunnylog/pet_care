from django.db import models
from users.models import User

class SitterComment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # pr? = models.ForeignKey(PR?, on_delete=models.CASCADE)
    # updated_at 처리는 어떻게?
    content = models.TextField()

    def __str__(self):
        return str(self.content)
