from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from .views import PostView, GroupView, CommentView

router = SimpleRouter()
router.register('posts', PostView)
router.register('groups', GroupView)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentView)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
