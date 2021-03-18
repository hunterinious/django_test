from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    theme = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    picture = models.ImageField(upload_to="post_pictures", null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

