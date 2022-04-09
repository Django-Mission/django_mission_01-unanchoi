from hashlib import blake2b
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Post(models.Model):
    image = models.ImageField(verbose_name="이미지", null=True, blank=True)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    view_count = models.IntegerField(verbose_name="조회수", default=0)


class Comment(models.Model):
    content = models.TextField(verbose_name="내용", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="작성자", auto_now_add=True)
    post = models.ForeignKey(to="Post", on_delete=models.CASCADE)
    writer = models.ForeignKey(
        to=User, null=True, blank=True,  on_delete=models.CASCADE)
