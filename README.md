# Simulated Exposure Therapy – Implementation

This project demonstrates a functional prototype of **Simulated Exposure Therapy (SET)**. It provides a system for monitoring physiological stress levels in real-time and adjusting VR-based exposure scenarios dynamically to simulate therapeutic interventions.

The system integrates real-time sensor data, stress computation algorithms, AI-based emotion detection, and VR scene management for an interactive therapeutic experience.

---

## Features

* **Real-time stress monitoring**: Collect heart rate (HR) and galvanic skin response (GSR) using Python-based sensors.
* **Stress analysis algorithms**: Compute normalized stress levels and adapt exposure intensity.
* **AI emotion detection**: Predict user emotional state (calm, nervous, anxious) using a placeholder AI module.
* **VR integration**: Send real-time intensity adjustments to a VR client for immersive scenarios.
* **Dashboard UI**: Monitor stress levels, VR intensity, and system logs in real-time.

---

## Tech Stack

* **Backend**: FastAPI, WebSockets, Python
* **Frontend**: JavaScript (Chart.js) for real-time dashboards
* **VR Simulation**: Python-based VR client with configurable scenes
* **Sensors**: Simulated heart rate and GSR sensors in Python
* **AI Module**: Placeholder module (replaceable with CNN/RNN models for emotion detection)

---

## Getting Started

1. **Install dependencies**:

   ```bash
   pip install -r backend/requirements.txt
   ```

2. **Start the backend server**:

   ```bash
   uvicorn backend.main:app --reload
   ```

   Access dashboard at `http://127.0.0.1:8000/` (for basic connection check).

3. **Run VR client simulation**:

   ```bash
   python vr_client/vr_client.py
   ```

4. **Run stress sensor simulator**:

   ```bash
   python sensors/stress_sender.py
   ```

   The sensor simulator sends heart rate and GSR values to the backend via WebSockets.

---

## Project Structure

```
backend/              # FastAPI backend and models
  models/             # Stress processor, exposure algorithm, AI adapter
  main.py             # Backend entry point
sensors/              # Simulated sensor scripts
vr_client/            # VR client simulation scripts and scene configurations
index.html            # Dashboard UI (real-time charts)
tests/                # Unit tests
```

---

## How It Works

1. Sensor simulator sends physiological data (HR/GSR) to the backend.
2. Backend computes normalized stress level using `StressProcessor`.
3. AI module predicts user emotion from stress signals.
4. Exposure intensity is calculated based on stress level.
5. VR client receives real-time intensity updates to adjust the scenario.
6. Dashboard displays real-time stress and intensity charts for monitoring.

---

## Future Improvements

* Replace the dummy AI module with a real CNN/RNN model for emotion detection.
* Integrate real VR hardware for immersive therapy.
* Add user authentication and session management for patient tracking.
* Store historical stress and VR data in a database for analysis.

---

## License

MIT License
