import asyncio
import websockets

async def echo(websocket, path):
    # When a client connects, this function will be called with the WebSocket
    # object representing the connection and the request path.

    # Print a message to indicate the connection
    print(f"Client connected from {websocket.remote_address}")

    try:
        # Continuously listen for messages from the client
        async for message in websocket:
            print("Message:", message)
            # Echo the received message back to the client
            await websocket.send(message + "response")
    finally:
        # When the connection is closed, print a message
        print(f"Client disconnected from {websocket.remote_address}")

# Start the WebSocket server
start_server = websockets.serve(echo, "localhost", 8765)

# Run the event loop to start the server
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()