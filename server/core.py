def compute_operation(op: str, a: float, b: float) -> float:
    """
    Perform basic arithmetic operations.

    Args:
        op: The operation name (add, subtract, multiply, divide).
        a: The first number.
        b: The second number.

    Returns:
        The result of the operation.

    Raises:
        ValueError: If the operation is unknown or if dividing by zero.
    """
    if op == "add":
        return a + b
    elif op == "subtract":
        return a - b
    elif op == "multiply":
        return a * b
    elif op == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Unknown operation: {op}")
