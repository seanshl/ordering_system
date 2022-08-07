from typing import List
from datetime import datetime
from .models import Commodity, SeckillCampaign


def load_commodity_by_id(commodity_id: int) -> Commodity:
    commodity = Commodity.objects.get(id=commodity_id)
    return commodity


def list_commodity(
    commodity_id=None,
    commodity_name=None,
) -> List[Commodity]:
    if not commodity_id and not commodity_name:
        return []
    elif not commodity_name:
        commodity_list = Commodity.objects.filter(id=commodity_id)
    elif not commodity_id:
        commodity_list = Commodity.objects.filter(commodity_name=commodity_name)
    else:
        commodity_list = Commodity.objects.filter(
            id=commodity_id, commodity_name=commodity_name
        )
    return list(commodity_list)


def create_commodity(
    commodity_name: str,
    price: int,
    commodity_description: str,
) -> Commodity:
    new_commodity = Commodity(
        commodity_name=commodity_name,
        commodity_description=commodity_description,
        commodity_price=price,
    )
    new_commodity.save()
    return new_commodity.id


def update_commodity(
    commodity_id,
    commodity_name=None,
    price=None,
    commodity_description=None,
) -> Commodity:
    # import ipdb; ipdb.set_trace()

    commodity = load_commodity_by_id(commodity_id)
    if commodity:
        if commodity_name:
            commodity.commodity_name = commodity_name
        if price:
            commodity.commodity_price = price
        if commodity_description:
            commodity.commodity_description = commodity_description
        commodity.save()


def load_seckill_campaign_by_id(seckill_campaign_id: int) -> SeckillCampaign:
    seckill_campaign = SeckillCampaign.objects.get(id=seckill_campaign_id)
    return seckill_campaign


def list_seckill_campaigns_by_status(campaign_status) -> List[SeckillCampaign]:
    if campaign_status not in (0, 1, 2):
        raise Exception("Invalid status!")
    campaign_list = SeckillCampaign.objects.filter(campaign_status=campaign_status)
    return list(campaign_list)


def create_seckill_campaign(
    campaign_name,
    commodity,
    original_price=0,
    seckill_price=0,
    start_time=None,
    end_time=None,
    total_stock=0,
    available_stock=0,
) -> SeckillCampaign:
    new_campaign = SeckillCampaign(
        campaign_name=campaign_name,
        commodity=commodity,
        original_price=original_price,
        seckill_price=seckill_price,
        campaign_status=2,
        start_time=start_time,
        end_time=end_time,
        total_stock=total_stock,
        available_stock=available_stock,
        lock_stock=0,
    )
    new_campaign.save()
    return new_campaign.id


def update_seckill_campaign(
    seckill_campaign_id,
    campaign_name=None,
    original_price=None,
    seckill_price=None,
    campaign_status=None,
    start_time=None,
    end_time=None,
    total_stock=None,
    available_stock=None,
    lock_stock=None,
):
    seckill_campaign = load_seckill_campaign_by_id(seckill_campaign_id)

    if campaign_name:
        seckill_campaign.campaign_name = campaign_name
    if original_price:
        seckill_campaign.original_price = original_price
    if seckill_price:
        seckill_campaign.seckill_price = seckill_price
    if campaign_status:
        if campaign_status not in (0, 1, 2):
            raise Exception("invalid stauts!")
        else:
            seckill_campaign.campaign_status = campaign_status
    if start_time:
        start_time = datetime.strptime(
            start_time.replace(" ", "-"), "%Y-%m-%d-%H:%M:%S"
        )
        seckill_campaign.start_time = start_time
    if end_time:
        end_time = datetime.strptime(end_time.replace(" ", "-"), "%Y-%m-%d-%H:%M:%S")
        seckill_campaign.end_time = end_time
    if total_stock:
        seckill_campaign.total_stock = total_stock
    if available_stock:
        seckill_campaign.available_stock = available_stock
    if lock_stock:
        seckill_campaign.lock_stock = lock_stock

    seckill_campaign.save()
