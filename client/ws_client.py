import asyncio
import json
import logging
import websockets
from typing import Optional, Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ws_client")


class WebSocketClient:
    def __init__(self, uri: str):
        self.uri = uri
        self.websocket = None

    async def connect(self):
        try:
            self.websocket = await websockets.connect(self.uri)
            logger.info(f"Connected to {self.uri}")
        except Exception as e:
            logger.error(f"Failed to connect: {e}")
            raise

    async def disconnect(self):
        if self.websocket:
            await self.websocket.close()
            logger.info("Disconnected")

    async def compute(
        self, operation: str, a: float, b: float
    ) -> Optional[Dict[str, Any]]:
        if not self.websocket:
            await self.connect()

        payload = {"operation": operation, "a": a, "b": b}

        try:
            await self.websocket.send(json.dumps(payload))
            response = await self.websocket.recv()
            return json.loads(response)
        except websockets.exceptions.ConnectionClosed:
            logger.error("Connection closed unexpectedly")
            return None
        except Exception as e:
            logger.error(f"Error during computation: {e}")
            return None
