"""Package for volumetric flow rate-related classes and constants."""

from .exceptions import ZeroTimeIntervalDivisionError
from .volumetric_flow_rate import VolumetricFlowRate

__all__ = ["VolumetricFlowRate", "ZeroTimeIntervalDivisionError"]
