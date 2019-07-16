from aiohttp import web
from guillotina import configure
from guillotina.interfaces import IResource
from guillotina.api.service import Service
from guillotina.component import get_utility
from guillotina.interfaces import IPubSubUtility
from functools import partial

import aiohttp
import logging


async def pubsub_callback(ws, data, sender=None):
    await ws.send_str(data)


@configure.service(context=IResource, method='GET', name='@content-changes',
                   permission='guillotina.AccessContent')
async def ws_conversate(context, request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    util = get_utility(IPubSubUtility)
    await util.subscribe(
        'test_channel', request.uid, partial(pubsub_callback, ws)
    )

    async for _ in ws:
        pass
    return {}