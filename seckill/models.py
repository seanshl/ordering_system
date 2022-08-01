from django.db import models

class Seckill_activity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    commodity_id = models.BigIntegerField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    seckill_price = models.DecimalField(max_digits=10, decimal_places=2)
    activity_status = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    total_stock = models.PositiveBigIntegerField()
    available_stock = models.IntegerField()
    lock_stock = models.PositiveBigIntegerField(default=0)
    indexes = [
        models.Index(name='id_name_commodity_idx', fields=['id', 'name', 'commodity_id']),
        models.Index(name='name_idx', fields=['name'])
    ]


