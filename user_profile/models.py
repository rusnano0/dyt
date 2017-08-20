from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    username = models.CharField('username', max_length = 20, unique = True, db_index = True)
    email = models.EmailField('email address', unique = True)
    joined = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

