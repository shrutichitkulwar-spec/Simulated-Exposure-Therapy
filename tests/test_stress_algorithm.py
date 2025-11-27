from backend.models.exposure_algorithm import get_intensity

def test_algorithm():
    assert get_intensity(0.1) == 1.0
    assert get_intensity(0.3) == 0.7
    assert get_intensity(0.6) == 0.4
    assert get_intensity(0.9) == 0.2
