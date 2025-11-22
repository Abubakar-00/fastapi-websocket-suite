import json

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

from server.core import compute_operation
from server.schemas import ComputeRequest, ComputeResponse, ErrorResponse
from server.utils import logger

app = FastAPI(title="WebSocket Compute Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """
    Simple health check endpoint to verify server status.
    """
    return {"status": "ok"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for handling computation requests.
    Accepts JSON messages with 'operation', 'a', and 'b', and returns the result.
    """
    await websocket.accept()
    logger.info("Client connected")
    try:
        while True:
            data = await websocket.receive_text()
            try:
                payload = json.loads(data)
                request = ComputeRequest(**payload)

                result = compute_operation(request.operation, request.a, request.b)

                response = ComputeResponse(
                    operation=request.operation, a=request.a, b=request.b, result=result
                )
                await websocket.send_json(response.model_dump())
                logger.info(
                    f"Computed: {request.operation}({request.a}, {request.b}) = {result}"
                )

            except json.JSONDecodeError:
                logger.warning("Received invalid JSON")
                await websocket.send_json(
                    ErrorResponse(error="Invalid JSON").model_dump()
                )
            except ValidationError as e:
                logger.warning(f"Validation error: {e}")
                await websocket.send_json(ErrorResponse(error=str(e)).model_dump())
            except ValueError as e:
                logger.warning(f"Value error: {e}")
                await websocket.send_json(ErrorResponse(error=str(e)).model_dump())
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                await websocket.send_json(
                    ErrorResponse(error="Internal server error").model_dump()
                )

    except WebSocketDisconnect:
        logger.info("Client disconnected")
