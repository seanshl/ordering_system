from seckill.models import Commodity
from rest_framework import serializers


class CommoditySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commodity
        fields = [
            "id",
            "commodity_name",
            "commodity_description",
            "commodity_price",
        ]
