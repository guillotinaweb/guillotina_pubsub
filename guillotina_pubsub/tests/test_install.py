import asyncio


async def test_install(guillotina_pubsub_requester):  # noqa
    async with guillotina_pubsub_requester as requester:
        response, _ = await requester('GET', '/db/guillotina/@addons')
        assert 'guillotina_pubsub' in response['installed']
