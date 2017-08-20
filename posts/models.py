from django.db import models
from user_profile.models import User

class Post(models.Model):
    ''' Post model '''
    user = models.ForeignKey(User)
    text = models.CharField(max_length = 300)
    created_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=30, default='Global')
    is_active = models.BooleanField(default = True)
    is_favorite = models.BooleanField(default = False)

    def __str__(self):
        return self.text[:50]


class HashTag(models.Model):
    ''' HashTag model '''
    name = models.CharField(max_length = 100, unique = True)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.name

