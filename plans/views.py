from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Tag, Plan, BucketList
from .serializers import (TagSerializer, PlanSerializer, PlanDetailSerializer,
                          BucketListSerializer)


# ModelViewSet 클래스에 비해, mixin 클래스를 사용하면 보다 유연하다.
class TagViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    """ 데이터베이스의 태그를 관리한다. """
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # ListModelMixin 클래스의 list 메소드가 호출되면, 즉 URL 주소에 의해 TagViewSet 클래스가 호출되면,
    # GenericAPIView 클래스의 get_queryset 메소드를 통해 데이터베이스에서 태그 인스턴스들을 가져오게 된다.
    # 따라서, 이 함수를 변경함으로써 원하는 태그 인스턴스들만 반환하도록 커스터마이징 할 수 있다.
    def get_queryset(self):
        """ 현재 인증되어 있는 사용자에 의해 생성된 태그 인스턴스만 보여준다. """
        return self.queryset.filter(user=self.request.user).order_by('-name')

    # 올바론 사용자에게 태그 인스턴스를 할당하기 위해서, CreateModelMixin 클래스에 포함된
    # perform_create 메소드를 오버라이딩한다. (serializer.save()에 kwargs 지정하는 방식)
    # serializer.save()는 유효성 검사(Validation)가 완료된 데이터를 데이터베이스에 저장하는 함수이다.
    def perform_create(self, serializer):
        """ 새로운 태그를 생성하고, 그 태그에 현재 사용중인 유저를 연결한다. """
        serializer.save(user=self.request.user)


# 일정 모델은 CRUD 기능을 모두 제공할 예정이므로, ModelViewSet 클래스 사용.
class PlanViewSet(viewsets.ModelViewSet):
    """ 데이터베이스의 일정을 관리한다. """
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    # def get_queryset(self):
    #     """ 인증되어 있는 사용자에 해당하는 일정 인스턴스만 반환한다. """
    #     return self.queryset.filter(user=self.request.user)

    # ViewSet 클래스에서 지원하는 다양한 행동(List, Create 등) 중, 일정 행동에 대해서
    # 다른 시리얼라이저를 사용할 수 있도록 get_serializer_class 메소드를 오버라이드한다.
    def get_serializer_class(self):
        """ 행동에 따라 적절한 시리얼라이저 클래스를 반환한다. """
        if self.action == 'retrieve':
            return PlanDetailSerializer
        return PlanSerializer

    def perform_create(self, serializer):
        """ 새로운 일정을 생성하고, 현재 사용중인 사용자를 연결한다. """
        serializer.save(user=self.request.user)


class BucketListViewSet(viewsets.ModelViewSet):
    """ 데이터베이스의 하고싶은 일 모델을 관리한다. """
    serializer_class = BucketListSerializer
    queryset = BucketList.objects.all().order_by('-date_created')
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        """ 새로운 일정을 생성하고, 현재 사용중인 사용자를 연결한다. """
        serializer.save(user=self.request.user, profile=self.request.user.profile)

    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user, profile=self.request.user.profile)
