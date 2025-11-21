from typing import Literal

from pydantic import BaseModel


class ComputeRequest(BaseModel):
    operation: Literal["add", "subtract", "multiply", "divide"]
    a: float
    b: float


class ComputeResponse(BaseModel):
    operation: str
    a: float
    b: float
    result: float


class ErrorResponse(BaseModel):
    error: str
