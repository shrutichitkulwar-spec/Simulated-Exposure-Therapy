document.addEventListener("DOMContentLoaded", () => {
    const connectBtn = document.getElementById("connectBtn");
    const heartRateEl = document.getElementById("heartRate");
    const stressLevelEl = document.getElementById("stressLevel");
    const vrIntensityEl = document.getElementById("vrIntensity");
    const vrSceneEl = document.getElementById("vrScene");

    let currentIntensity = 0;
    let targetIntensity = 0;

    connectBtn.addEventListener("click", () => {
        connectBtn.disabled = true;
        connectBtn.innerText = "CONNECTED";

        // Sensor WebSocket
        const sensorSocket = new WebSocket("ws://127.0.0.1:8001/ws/sensor");

        sensorSocket.onopen = () => {
            console.log("Sensor WebSocket connected");

            setInterval(() => {
                const sensorData = {
                    heart_rate: Math.floor(60 + Math.random() * 40),
                    gsr: Math.random()
                };
                sensorSocket.send(JSON.stringify(sensorData));
            }, 1000);
        };

        sensorSocket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            heartRateEl.innerText = data.heart_rate;
            stressLevelEl.innerText = data.stress_level.toFixed(2);

            // Update target intensity for VR
            targetIntensity = data.stress_level;

            // Send to VR WebSocket
            if (vrSocket.readyState === WebSocket.OPEN) {
                vrSocket.send(JSON.stringify({ stress_level: targetIntensity }));
            }
        };

        // VR WebSocket
        const vrSocket = new WebSocket("ws://127.0.0.1:8001/ws/vr");

        vrSocket.onopen = () => {
            console.log("VR WebSocket connected");
        };

        vrSocket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            targetIntensity = data.new_intensity;
            vrIntensityEl.innerText = targetIntensity.toFixed(2);
        };

        // Smooth animation for VR Scene
        function animateVR() {
            currentIntensity += (targetIntensity - currentIntensity) * 0.05; // easing
            const size = 100 + currentIntensity * 100; // circle 100px to 200px
            vrSceneEl.style.width = size + "px";
            vrSceneEl.style.height = size + "px";

            // Gradient color: green -> yellow -> red
            const red = Math.round(currentIntensity * 255);
            const green = Math.round(255 - currentIntensity * 255);
            vrSceneEl.style.backgroundColor = `rgb(${red}, ${green}, 200)`;

            vrSceneEl.innerText = `${Math.round(currentIntensity * 100)}%`;

            requestAnimationFrame(animateVR);
        }

        animateVR();

        sensorSocket.onclose = vrSocket.onclose = () => {
            console.log("WebSocket disconnected");
            connectBtn.innerText = "CONNECT TO BACKEND";
        };
    });
});
