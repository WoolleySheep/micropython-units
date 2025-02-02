import unittest

from units import VolumeUnit, volume


class ZeroTest(unittest.TestCase):
    """Unit tests for zero volume."""

    def test_zero_volume_value(self):
        self.assertAlmostEqual(0, volume.ZERO.as_unit(VolumeUnit.CUBIC_METER))
