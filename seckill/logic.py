from .data_access import list_commodity
from .data_access import update_commodity


def update_commodity_price_by_name(
    commodity_name,
    price,
):
    commodities = list_commodity(commodity_name=commodity_name)

    for commodity in commodities:
        update_commodity(
            commodity_id=commodity.id,
            price=price,
        )
