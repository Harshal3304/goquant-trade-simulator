import asyncio
import websockets
import json
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.orderbook import OrderBook
# from core.orderbook import OrderBook

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("WebSocketHandler")

WS_URL = "wss://ws.gomarket-cpp.goquant.io/ws/l2-orderbook/okx/BTC-USDT-SWAP"

class WebSocketHandler:
    def __init__(self, url=WS_URL):
        self.url = url
        self.connection = None
        self.orderbook = OrderBook()


    async def connect(self):
        try:
            self.connection = await websockets.connect(self.url)
            log.info("WebSocket connected.")
            await self.listen()
        except Exception as e:
            log.error(f"Connection error: {e}")

    async def listen(self):
        try:
            while True:
                message = await self.connection.recv()
                data = json.loads(message)
                self.process_data(data)
        except Exception as e:
            log.error(f"Listening error: {e}")

    def process_data(self, data):
        if "asks" in data and "bids" in data:
            self.orderbook.update(data)
            top_bid, top_ask = self.orderbook.get_top_of_book()
            log.info(f"📊 Top Bid: {top_bid} | Top Ask: {top_ask}")
        else:
            log.warning("Invalid format received.")

    async def close(self):
        if self.connection:
            await self.connection.close()
            log.info("WebSocket closed.")

if __name__ == "__main__":
    ws = WebSocketHandler()
    asyncio.run(ws.connect())
