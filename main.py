from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import json

from backend.models.exposure_algorithm import get_intensity
from backend.models.stress_processor import StressProcessor
from backend.models.ai_adapter import AIAdapter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instances
stress_processor = StressProcessor(sensitivity=0.5)
ai_model = AIAdapter(model_strength=0.8)

@app.get("/")
def home():
    return {"message": "Simulated Exposure Therapy Backend Running"}

@app.websocket("/ws/sensor")
async def sensor_websocket(websocket: WebSocket):
    await websocket.accept()
    print("Sensor connected")

    try:
        while True:
            data = await websocket.receive_text()
            sensor_data = json.loads(data)

            heart_rate = sensor_data.get("heart_rate", 80)
            gsr = sensor_data.get("gsr", 0.5)

            stress_level = stress_processor.normalize_stress(heart_rate, gsr)
            emotion = ai_model.predict_emotion(stress_level)

            await websocket.send_json({
                "stress_level": stress_level,
                "emotion": emotion
            })

    except WebSocketDisconnect:
        print("Sensor disconnected")

@app.websocket("/ws/vr")
async def vr_websocket(websocket: WebSocket):
    await websocket.accept()
    print("VR connected")

    try:
        while True:
            data = await websocket.receive_text()
            payload = json.loads(data)

            stress = payload.get("stress_level", 0.5)
            new_intensity = get_intensity(stress)

            await websocket.send_json({
                "new_intensity": new_intensity
            })

    except WebSocketDisconnect:
        print("VR disconnected")
