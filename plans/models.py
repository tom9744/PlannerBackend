from django.db import models
from django.conf import settings    # Django settings.py 파일의 설정에서 User 모델을 가져오는 방법.

from accounts.models import Profile


class Tag(models.Model):
    """ 일정에 사용될 태그 """
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = '태그'
        verbose_name_plural = '태그'

    def __str__(self):
        return self.name


class Plan(models.Model):
    """ 일정 모델 """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    # 필수 필드가 아닌것을 나타내기 위해 'blank=True'만 사용하는 것이 좋다. (검사 상의 편의를 위해)
    location = models.CharField(max_length=255, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_starts = models.DateField()
    date_ends = models.DateField()
    # ManyToManyField 매개변수에 따옴표를 사용하는 것이 좋다. (클래스의 위치를 맞추어주지 않아도 된다.)
    tags = models.ManyToManyField('Tag')

    is_complete = models.BooleanField(default=False)

    class Meta:
        verbose_name = '일정'
        verbose_name_plural = '일정'

    def __str__(self):
        return self.title


class BucketList(models.Model):
    """ 하고 싶은 일 모델 """
    Rating_CHOICES = (
        (0, '매우 중요하지 않음'),
        (1, '중요하지 않음'),
        (2, '중간'),
        (3, '중요함'),
        (4, '매우 중요함')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    importance = models.IntegerField(choices=Rating_CHOICES, default=2)

    date_created = models.DateField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    class Meta:
        verbose_name = '하고 싶은 일'
        verbose_name_plural = '하고 싶은 일'

    def __str__(self):
        return self.title