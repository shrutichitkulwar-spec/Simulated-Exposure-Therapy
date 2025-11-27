def get_intensity(stress: float) -> float:
    if stress > 0.75:
        return 0.2
    elif stress > 0.5:
        return 0.4
    elif stress > 0.25:
        return 0.7
    else:
        return 1.0
