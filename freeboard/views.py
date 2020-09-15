from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """ 데이터베이스의 게시물 모델을 관리한다. """
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, ]
    filter_backends = [SearchFilter, OrderingFilter, ]

    search_fields = ['is_complete']
    ordering = ['-id']

    # TODO Permission 추가를 통해 본인이 작성한 게시물만 지울 수 있도록 하기

    def perform_create(self, serializer):
        """ 새로운 일정을 생성하고, 현재 사용중인 사용자를 연결한다. """
        serializer.save(user=self.request.user, profile=self.request.user.profile)
