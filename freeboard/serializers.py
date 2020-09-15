from rest_framework import serializers

from .models import Post
from accounts.serializers import ProfileAvatarSerializer


class PostSerializer(serializers.ModelSerializer):
    """ 게시물 모델 시리얼라이저 """
    user = serializers.StringRelatedField(read_only=True)
    profile = ProfileAvatarSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'user', 'profile', 'title',
            'description', 'date_created', 'date_updated'
        )
        read_only_fields = ('id', 'date_created', 'date_updated')

    # TODO Validation 추가하기

