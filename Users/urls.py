from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import UserView

"""Build dynamic urls with routers"""

router = routers.DefaultRouter()
router.register("Users",UserView,basename="UserModel")

urlpatterns = [
    path("api/",include(router.urls)),
]
