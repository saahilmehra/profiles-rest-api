from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet,base_name='login')
router.register('feed',views.UserProfileFeedViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
