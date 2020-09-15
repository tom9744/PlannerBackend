from django.db import models
from django.conf import settings

from accounts.models import Profile


class Post(models.Model):
    """ 게시물 모델 """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField()

    # TODO DateTime 필드로 변경하기
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = '게시물'
        verbose_name_plural = '게시물'

    def __str__(self):
        return self.title


