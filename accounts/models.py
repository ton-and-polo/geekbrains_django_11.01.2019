from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    user_avatar = models.ImageField(
        upload_to='users_avatar/',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.username