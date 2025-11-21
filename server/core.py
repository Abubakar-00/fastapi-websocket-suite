def compute_operation(op: str, a: float, b: float) -> float:
    """
    Perform basic arithmetic operations.
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
