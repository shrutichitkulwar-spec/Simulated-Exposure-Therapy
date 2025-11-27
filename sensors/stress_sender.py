import websocket
import json
import time
import random

ws = websocket.create_connection("ws://localhost:8000/ws/stress")
print("Stress sender connected")

try:
    while True:
        stress = random.uniform(0, 1)
        msg = {"stress": stress}
        ws.send(json.dumps(msg))
        print("Sent stress:", stress)
        time.sleep(1)

except KeyboardInterrupt:
    ws.close()
