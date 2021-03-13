# users/urls.py

from django.urls import path,include
from users.views import dashboard

from rest_framework import routers
from .views import UploadViewSet,UserViewSet

router = routers.SimpleRouter()
router.register('user', UserViewSet, basename="users")
router.register('upload', UploadViewSet, basename="upload")


urlpatterns = [
    path("", include(router.urls)),
    path("dashboard", dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),


]