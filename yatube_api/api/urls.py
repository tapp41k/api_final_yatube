from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, GroupViewSet, FollowViewSet, PostViewSet


app_name = 'api'

router_v1 = routers.SimpleRouter()
router_v1.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(r'follow', FollowViewSet, basename='follow')
router_v1.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('v1/', include(router_v1.urls,)),
    path('v1/', include('djoser.urls.jwt')),
]
