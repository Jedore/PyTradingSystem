"""
    PyTradingSystem Base Protocol
"""

from asyncio import Protocol, transports
from typing import Optional


class PyTSProtocol(Protocol):
    __slots__ = ('transport',)

    def __init__(self):
        self.transport = transports.BaseTransport()

    def connection_made(self, transport: transports.BaseTransport) -> None:
        self.transport = transport
        print('connection_made')

    def connection_lost(self, exc: Optional[Exception]) -> None:
        print('connection lost')

    def data_received(self, data: bytes) -> None:
        print('received data')
        # 'Ctrl+C' from client
        if data == b'\xff\xf4\xff\xfd\x06':
            self.transport.close()

    def eof_received(self) -> Optional[bool]:
        ...
