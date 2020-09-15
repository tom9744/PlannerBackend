from rest_framework import serializers

from .models import Tag, Plan, BucketList
from accounts.serializers import ProfileAvatarSerializer


class TagSerializer(serializers.ModelSerializer):
    """ 태그 모델을 위한 시리얼라이저 """

    class Meta:
        model = Tag
        fields = ('id', 'name', )
        read_only_fields = ('id', )


class BucketListSerializer(serializers.ModelSerializer):
    """ 하고 싶은 일을 위한 시리얼라이저 """
    user = serializers.StringRelatedField(read_only=True)
    profile = ProfileAvatarSerializer(read_only=True)

    class Meta:
        model = BucketList
        fields = ('id', 'user', 'profile', 'title', 'importance', 'date_created', 'is_complete')
        read_only_fields = ('id', 'date_created')


class PlanSerializer(serializers.ModelSerializer):
    """ 일정 모델을 위한 시리얼라이저 """

    user = serializers.StringRelatedField(read_only=True)
    profile = ProfileAvatarSerializer(read_only=True)
    # 태그 모델의 'Primary Key'를 이용하여 일정 모델에서 태그 모델을 표현한다.
    # tags = serializers.PrimaryKeyRelatedField(
    #     many=True,  # ManyToMany Relationship
    #     queryset=Tag.objects.all(),  # 사용할 쿼리셋
    # )

    class Meta:
        model = Plan
        fields = ('id', 'user', 'profile', 'title', 'description',
                  'location', 'date_created', 'date_starts', 'date_ends', 'is_complete')
        read_only_fields = ('id', 'user', 'profile', )

    def validate(self, attrs):
        difference = (attrs['date_ends'] - attrs['date_starts']).days
        if difference < 0:
            raise serializers.ValidationError("시작일이 종료일보다 이후일 수 없습니다.")
        return attrs


class PlanDetailSerializer(PlanSerializer):
    """ 일정의 세부내용을 위한 시리얼라이저 """

    # 기존에 작성한 시리얼라이저를 연결하여 해당 시리얼라이저에서 사용하는 필드를 바로 사용할 수도 있다.
    tags = TagSerializer(many=True, read_only=True)

