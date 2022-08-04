from django.urls import include, path
from rest_framework import routers
from seckill import views


router = routers.DefaultRouter()
router.register("commodity", views.CommodityViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
