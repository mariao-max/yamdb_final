from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, TitleViewSet, UserViewSet,
                       get_token_for_user, sign_up)

router = DefaultRouter()

router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register('users', UserViewSet)
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)
router.register('titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', sign_up),
    path('v1/auth/token/', get_token_for_user),
]
