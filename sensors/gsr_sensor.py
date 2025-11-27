import websocket
import json
import time
import random

ws = websocket.create_connection("ws://localhost:8000/ws/stress")
print("GSR Mock Sensor Connected")

try:
    while True:
        gsr = random.uniform(0.2, 1.2)
        normalized = min(max(gsr / 1.2, 0), 1)
        ws.send(json.dumps({"stress": normalized}))
        print(f"GSR={gsr:.2f} → Stress={normalized:.2f}")
        time.sleep(1)

except KeyboardInterrupt:
    ws.close()
