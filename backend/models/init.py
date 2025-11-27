"""
Models package for Simulated Exposure Therapy backend.
This package contains modular components such as:
- AI adapter (emotion/stress prediction)
- Stress signal processing
- Adaptive exposure level algorithm

These modules can be imported as:
    from backend.models import (
        AIAdapter,
        StressProcessor,
        ExposureController
    )
"""


from .stress_processor import normalize_stress, StressProcessor
from .exposure_algorithm import get_intensity
from .ai_adapter import AIAdapter

__all__ = [
    "AIAdapter",
    "StressProcessor",
    "ExposureController",
]
