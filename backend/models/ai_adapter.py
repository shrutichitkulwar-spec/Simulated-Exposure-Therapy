class AIAdapter:
    def __init__(self, model_strength: float = 1.0):
        self.model_strength = model_strength

    def predict_emotion(self, signal: float) -> str:
        """
        Dummy AI model. Replace with ML later.
        """
        signal = signal * self.model_strength

        if signal > 0.7:
            return "anxiety"
        elif signal > 0.4:
            return "nervous"
        else:
            return "calm"
