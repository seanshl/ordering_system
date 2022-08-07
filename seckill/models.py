from django.db import models
from datetime import datetime
import pytz


class Commodity(models.Model):
    id = models.BigAutoField(primary_key=True)
    commodity_name = models.CharField(max_length=50)
    commodity_description = models.CharField(max_length=1000)
    commodity_price = models.IntegerField(default=0)

    def get_commodity_price_in_dollar(self):
        return self.commodity_price / 100


class CampaignStatus(models.IntegerChoices):
    ACTIVE = 0
    INACTIVE = 1


class SeckillCampaign(models.Model):
    class Meta:
        db_table = "seckill_campaign"

    id = models.BigAutoField(primary_key=True)
    campaign_name = models.CharField(max_length=200)
    # commodity_id = models.BigIntegerField(de)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    original_price = models.IntegerField(default=0)
    seckill_price = models.IntegerField(default=0)  # Use cents
    campaign_status = models.IntegerField(default=0, choices=CampaignStatus)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    total_stock = models.IntegerField(default=0)
    available_stock = models.IntegerField(default=0)
    lock_stock = models.IntegerField(default=0)
    # indexes = [
    #     models.Index(name='id_name_commodity_idx', fields=['id', 'name', 'commodity_id']),
    #     models.Index(name='name_idx', fields=['name'])
    # ]

    def is_expired(self):
        return self.end_time and datetime.now(pytz.utc) > self.end_time

    def is_active(self):
        return self.campaign_status == CampaignStatus.ACTIVE

    def has_started(self):
        return datetime.now(pytz.utc) >= self.start_time

    def is_running(self):
        return self.has_started() and (not self.is_expired())
