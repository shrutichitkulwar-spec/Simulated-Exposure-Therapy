import websocket
import json
import time
import random

ws = websocket.create_connection("ws://localhost:8000/ws/stress")
print("Heart Rate Mock Sensor Connected")

try:
    while True:
        hr = random.randint(60, 130)
        normalized = (hr - 60) / 70
        msg = {"stress": normalized}
        ws.send(json.dumps(msg))
        print(f"HR={hr} → Stress={normalized:.2f}")
        time.sleep(1)

except KeyboardInterrupt:
    ws.close()
