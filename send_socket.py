import asyncio
import websockets
import json

async def send_event():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = {"function": "meeting_acceptance", "user": "wahib"}

        # Sending the JSON message
        await websocket.send(json.dumps(message))
        print(f"Sent message: {message}")

        # Receive a response (if any)
        try:
            response = await websocket.recv()
            print(f"Received from server: {response}")
        except Exception as e:
            print(f"Error receiving message: {e}")

# Run the client
asyncio.run(send_event())
