import asyncio

from django.shortcuts import render

from .models import SensehatReading


# ------------------------------------------------------------------------------
async def _get_total():
    return SensehatReading.objects.all().count()


# ------------------------------------------------------------------------------
async def _get_total_mqtt():
    return SensehatReading.objects.filter(source=0).count()


# ------------------------------------------------------------------------------
async def _get_total_websocket():
    return SensehatReading.objects.filter(source=1).count()


def dashboard(request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = (_get_total_mqtt(), _get_total_websocket(), _get_total())

    keys = ['total_mqtt', 'total_websocket', 'total']
    totals = dict(zip(keys, loop.run_until_complete(asyncio.gather(*tasks))))
    loop.close()
    args = {'nav_item': {'main': 'Dashboard'},
            'totals': totals,}
    return render(request, 'operations/dashboard.html', args)
