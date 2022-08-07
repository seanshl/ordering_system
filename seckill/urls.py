from django.urls import path

from . import views

urlpatterns = [
    path("", views.seckill_campaigns_list),  # list
    path("seckill-campaign/", views.seckill_campaign_view),  # show or add new
]
