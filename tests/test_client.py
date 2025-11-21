import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from client.ws_client import WebSocketClient
import json


@pytest.mark.asyncio
async def test_client_connect():
    client = WebSocketClient("ws://test")
    with patch("websockets.connect", new_callable=AsyncMock) as mock_connect:
        await client.connect()
        mock_connect.assert_called_once_with("ws://test")


@pytest.mark.asyncio
async def test_client_compute():
    client = WebSocketClient("ws://test")
    client.websocket = AsyncMock()

    expected_response = {"operation": "add", "a": 1, "b": 2, "result": 3}
    client.websocket.recv.return_value = json.dumps(expected_response)

    result = await client.compute("add", 1, 2)

    client.websocket.send.assert_called_once()
    assert result == expected_response
