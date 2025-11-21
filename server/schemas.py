from pydantic import BaseModel
from typing import Literal


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
