from typing import List
from datetime import datetime

from seckill.exceptions import CommodityNotExistError
from .models import CampaignStatus, Commodity, SeckillCampaign
import pytz


def load_commodity_by_id(commodity_id: int) -> Commodity:
    commodity = Commodity.objects.get(id=commodity_id)
    return commodity


def list_commodities(
    commodity_id: int = None,
    commodity_name: int = None,
) -> List[Commodity]:
    query = Commodity.objects.filter()
    if commodity_name:
        query = query.filter(commodity_name=commodity_name)
    if commodity_id:
        query = query.filter(id=commodity_id)

    return list(query.all())


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
    else:
        raise CommodityNotExistError(
            "Commodity for id {} does not exist".format(update_commodity)
        )


def list_seckill_campaigns(
    id: int = None,
    campaign_name: str = None,
    campaign_status: str = None,
) -> List[SeckillCampaign]:
    query = SeckillCampaign.objects.filter()
    # TODO add filtering by other fields

    return list(query.all())


def load_seckill_campaign_by_id(seckill_campaign_id: int) -> SeckillCampaign:
    seckill_campaign = SeckillCampaign.objects.get(id=seckill_campaign_id)
    return seckill_campaign


def list_seckill_campaigns_by_status(campaign_status) -> List[SeckillCampaign]:
    if campaign_status not in (0, 1, 2):
        raise Exception("Invalid status!")
    campaign_list = SeckillCampaign.objects.filter(campaign_status=campaign_status)
    return list(campaign_list)


def create_seckill_campaign(
    campaign_name: str,
    commodity_id: int,
    original_price: int = 0,
    seckill_price: int = 0,
    start_time: datetime = None,
    end_time: datetime = None,
    total_stock: int = 0,
    available_stock: int = 0,
) -> SeckillCampaign:
    new_campaign = SeckillCampaign.objects.create(
        campaign_name=campaign_name,
        commodity_id=commodity_id,
        original_price=original_price,
        seckill_price=seckill_price,
        campaign_status=2,
        start_time=start_time if start_time else datetime.now(pytz.utc),
        end_time=end_time,  # If end time is None, it means the campaign will last forever
        total_stock=total_stock,
        available_stock=available_stock,
        lock_stock=0,
    )
    # new_campaign.save()
    return new_campaign


def update_seckill_campaign(
    seckill_campaign_id,
    campaign_name: str = None,
    original_price: int = None,
    seckill_price: int = None,
    campaign_status: CampaignStatus = None,
    start_time: datetime = None,
    end_time: datetime = None,
    total_stock: int = None,
    available_stock: int = None,
    lock_stock: int = None,
) -> SeckillCampaign:
    seckill_campaign = load_seckill_campaign_by_id(seckill_campaign_id)

    if campaign_name:
        seckill_campaign.campaign_name = campaign_name
    if original_price:
        seckill_campaign.original_price = original_price
    if seckill_price:
        seckill_campaign.seckill_price = seckill_price
    if campaign_status:
        # if campaign_status not in (0, 1, 2):
        #     raise Exception("invalid stauts!")
        # else:
        seckill_campaign.campaign_status = campaign_status
    if start_time:
        # start_time = datetime.strptime(
        #     start_time.replace(" ", "-"), "%Y-%m-%d-%H:%M:%S"
        # )
        seckill_campaign.start_time = start_time
    if end_time:
        # end_time = datetime.strptime(end_time.replace(" ", "-"), "%Y-%m-%d-%H:%M:%S")
        seckill_campaign.end_time = end_time
    if total_stock:
        seckill_campaign.total_stock = total_stock
    if available_stock:
        seckill_campaign.available_stock = available_stock
    if lock_stock:
        seckill_campaign.lock_stock = lock_stock

    seckill_campaign.save()
    return seckill_campaign
