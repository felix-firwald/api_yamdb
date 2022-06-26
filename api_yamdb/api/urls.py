from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    TitleViewSet,
    ReviewViewSet
)

VERSION = 'v1/'
URL_ROOT_TITLE_ID = r'^titles/(?P<post_id>\d+)/'

router_v1 = DefaultRouter()

router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register(
    f'{URL_ROOT_TITLE_ID}reviews',
    ReviewViewSet,
    basename='reviews'
)

urlpatterns = [
    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        VERSION,
        include(router_v1.urls)
    ),
]
