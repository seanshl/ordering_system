from .models import Commodity
from typing import List


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
