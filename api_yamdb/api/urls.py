from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.authtoken import views

from .views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    TitleViewSet,
    UserViewSet,
    signup,
    token,
    code
)

VERSION = 'v1/'
URL_ROOT_TITLE_ID = r'^titles/(?P<post_id>\d+)/'
REVIEW_ID = r'(?P<review_id>\d+)/comments'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register(
    f'{URL_ROOT_TITLE_ID}reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    f'{URL_ROOT_TITLE_ID}reviews/{REVIEW_ID}',
    CommentViewSet, basename='comments'
)


urlpatterns = [
    path(
        VERSION,
        include(router_v1.urls)
    ),
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', token, name='login'),
    path('v1/auth/code/', code, name='code'),
]
