from rest_framework import viewsets
from seckill.models import Commodity
from seckill.serializers import CommoditySerializer

# Create your views here.


class CommodityViewSet(viewsets.ModelViewSet):
    queryset = Commodity.objects.all().order_by("id")
    serializer_class = CommoditySerializer
