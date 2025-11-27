import websocket
import json

def on_message(ws, message):
    data = json.loads(message)
    if data["command"] == "SET_INTENSITY":
        print(f"[VR] Exposure Intensity → {data['value']}")

def on_open(ws):
    print("VR Client Connected")

ws = websocket.WebSocketApp(
    "ws://localhost:8000/ws/client",
    on_open=on_open,
    on_message=on_message
)

ws.run_forever()
