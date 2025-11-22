from typing import Literal

from pydantic import BaseModel


class ComputeRequest(BaseModel):
    """
    Schema for incoming computation requests.
    """

    operation: Literal["add", "subtract", "multiply", "divide"]
    a: float
    b: float


class ComputeResponse(BaseModel):
    """
    Schema for successful computation responses.
    """

    operation: str
    a: float
    b: float
    result: float


class ErrorResponse(BaseModel):
    """
    Schema for error responses.
    """

    error: str
