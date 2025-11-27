class StressProcessor:
    def __init__(self, sensitivity: float = 0.5):
        self.sensitivity = sensitivity

    def normalize_stress(self, value: float) -> float:
        """
        Normalize stress to 0–1 range with sensitivity.
        """
        # scale input
        value = value * self.sensitivity

        if value < 0:
            value = 0
        if value > 1:
            value = 1

        return value
