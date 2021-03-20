from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class PostManager(models.Manager):
    def delete_related_comments(self, post):
        post.comment_set.all().delete()
        post.save()


class Post(models.Model):
    theme = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    picture = models.ImageField(upload_to="post_pictures", null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = PostManager()

    def __str__(self):
        return self.theme


class Comment(models.Model):
    text = models.TextField(null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
