from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

# DefaultRouter 클래스는 작성한 ViewSet 클래스에 알맞는 URL 엔드포인트를 자동으로 생성해준다.
router = DefaultRouter()
router.register('tag', views.TagViewSet)
router.register('plan', views.PlanViewSet)
router.register('bucket-list', views.BucketListViewSet)

app_name = 'plans'

urlpatterns = [
    path('', include(router.urls)),
]
