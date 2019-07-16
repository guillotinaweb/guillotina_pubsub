from guillotina import configure
from guillotina import app_settings
from guillotina.interfaces import (IResource, IObjectModifiedEvent)
from guillotina.component import get_utility
from guillotina.interfaces import IPubSubUtility

import json

@configure.subscriber(for_=(IResource, IObjectModifiedEvent))
async def objectModify(obj, event):
    util = get_utility(IPubSubUtility)
    await util.publish("test_channel","process",json.dumps({
        'id': obj.id,
        'uuid': obj.__uuid__,
        'payload': event.payload
    }))
