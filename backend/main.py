from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import json

# Import your models
from backend.models.stress_processor import StressProcessor
from backend.models.exposure_algorithm import get_intensity
from backend.models.ai_adapter import AIAdapter

app = FastAPI()

# Allow your frontend to access the backend
origins = ["*"]  # For dev; in production, specify your frontend URL

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.get("/connect")
async def connect():
    return {"message": "Connected to backend!", "value": 42}

# WebSocket for sensor data
@app.websocket("/ws/sensor")
async def sensor_ws(websocket: WebSocket):
    await websocket.accept()
    print("Sensor connected")
    try:
        while True:
            data = await websocket.receive_text()
            sensor = json.loads(data)
            heart_rate = sensor.get("heart_rate", 80)
            gsr = sensor.get("gsr", 0.5)
            stress_level = min(1.0, max(0.0, (heart_rate - 60)/60 + gsr/2))
            await websocket.send_json({
                "stress_level": stress_level,
                "heart_rate": heart_rate
            })
    except WebSocketDisconnect:
        print("Sensor disconnected")

# WebSocket for VR intensity
@app.websocket("/ws/vr")
async def vr_ws(websocket: WebSocket):
    await websocket.accept()
    print("VR connected")
    try:
        while True:
            data = await websocket.receive_text()
            payload = json.loads(data)
            stress = payload.get("stress_level", 0.5)
            new_intensity = min(1.0, stress)
            await websocket.send_json({"new_intensity": new_intensity})
    except WebSocketDisconnect:
        print("VR disconnected")
