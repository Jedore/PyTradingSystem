"""
    PyTradingSystem Servers
"""
import asyncio

from config import ORDER_SERVER, OFFER_SERVER
from protocols import PyTSOrderProtocol, PyTSOfferProtocol


async def serve_order():
    """ Create order server """
    host, port = ORDER_SERVER.split(':')
    loop = asyncio.get_running_loop()
    order_server = await loop.create_server(PyTSOrderProtocol,
                                            host=host,
                                            port=int(port))
    print('OrderServer:', ORDER_SERVER)


async def serve_offer():
    """ Create offer server """
    loop = asyncio.get_running_loop()
    host, port = OFFER_SERVER.split(':')
    offer_server = await loop.create_server(PyTSOfferProtocol,
                                            host=host,
                                            port=int(port))
    print('OfferServer:', OFFER_SERVER)
