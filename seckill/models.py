from django.db import models


class SeckillCampaign(models.Model):
    id = models.BigAutoField(primary_key=True)
    campaign_name = models.CharField(max_length=200)
    # commodity_id = models.BigIntegerField()
    # original_price = models.DecimalField(max_digits=10, decimal_places=2)
    seckill_price = models.IntegerField(default=0)  # Use sents
    campaign_status = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    total_stock = models.IntegerField(default=0)
    available_stock = models.IntegerField(default=0)
    lock_stock = models.IntegerField(default=0)
    # indexes = [
    #     models.Index(name='id_name_commodity_idx', fields=['id', 'name', 'commodity_id']),
    #     models.Index(name='name_idx', fields=['name'])
    # ]
