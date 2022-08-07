from django.http import HttpResponse
from django.forms.models import model_to_dict
from seckill.logic import (
    add_seckill_campaign,
    available_seckill_campaigns_list,
    seckill_campaign_item_info,
)


def seckill_campaigns_list(request):
    campaigns_list = available_seckill_campaigns_list()
    res = dict()
    res["campaigns_list"] = campaigns_list
    return HttpResponse([model_to_dict(campaign) for campaign in campaigns_list])


def seckill_campaign_view(request):
    print("hello")
    if request.method == "GET":
        # import ipdb; ipdb.set_trace()
        campaign_id = request.GET.get("id", None)
        campaign = seckill_campaign_item_info(campaign_id)
        return HttpResponse(model_to_dict(campaign))
    else:
        campaign_name = request.POST.get("campaign_name", None)
        commodity_id = request.POST.get("commodity_id", None)
        original_price = request.POST.get("original_price", None)
        seckill_price = request.POST.get("seckill_price", None)
        start_time = request.POST.get("start_time", None)
        end_time = request.POST.get("end_time", None)
        stock = request.POST.get("stock", None)

        new_campaign = add_seckill_campaign(
            campaign_name,
            commodity_id,
            original_price,
            seckill_price,
            start_time,
            end_time,
            stock,
        )

        return HttpResponse("Success! The campaign id is %s" % (new_campaign.id))
