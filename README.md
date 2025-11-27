# Simulated Exposure Therapy – Implementation

This project demonstrates a functional prototype of Simulated Exposure Therapy using:

- FastAPI backend
- Real-time WebSockets
- Stress analysis algorithms
- VR client simulation (Python)

## How to Run
1. Install dependencies:
   pip install -r backend/requirements.txt

2. Start backend:
   uvicorn backend.main:app --reload

3. Start VR client:
   python vr_client/vr_client.py

4. Start stress simulator:
   python sensors/stress_sender.py
