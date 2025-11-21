import argparse
import asyncio
import random
from client.ws_client import WebSocketClient

async def run_single_operation(uri: str, operation: str, a: float, b: float):
    client = WebSocketClient(uri)
    try:
        await client.connect()
        result = await client.compute(operation, a, b)
        if result:
            if "error" in result:
                print(f"Error: {result['error']}")
            else:
                print(f"Result: {result['result']}")
    finally:
        await client.disconnect()

async def run_demo(uri: str):
    client = WebSocketClient(uri)
    operations = ["add", "subtract", "multiply", "divide"]
    try:
        await client.connect()
        print("Running demo mode...")
        for _ in range(5):
            op = random.choice(operations)
            a = round(random.uniform(1, 100), 2)
            b = round(random.uniform(1, 100), 2)
            
            # Edge case for divide by zero
            if op == "divide" and random.random() < 0.1:
                b = 0
            
            print(f"Requesting: {op}({a}, {b})")
            result = await client.compute(op, a, b)
            
            if result:
                if "error" in result:
                    print(f"  -> Error: {result['error']}")
                else:
                    print(f"  -> Result: {result['result']}")
            
            await asyncio.sleep(1)
    finally:
        await client.disconnect()

def main():
    parser = argparse.ArgumentParser(description="WebSocket Compute Client")
    parser.add_argument("--uri", default="ws://localhost:8000/ws", help="WebSocket URI")
    parser.add_argument("--operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")
    parser.add_argument("--a", type=float, help="First number")
    parser.add_argument("--b", type=float, help="Second number")
    
    args = parser.parse_args()
    
    if args.operation and args.a is not None and args.b is not None:
        asyncio.run(run_single_operation(args.uri, args.operation, args.a, args.b))
    else:
        asyncio.run(run_demo(args.uri))

if __name__ == "__main__":
    main()
