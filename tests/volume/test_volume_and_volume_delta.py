import unittest

from units import Volume, VolumeDelta, VolumeUnit


class VolumeAndVolumeDeltaTest(unittest.TestCase):
    """Unit tests for interactions between volume and volume delta classes."""

    def test_add_volume_delta_to_volume_produces_Volume(self) -> None:
        volume = Volume(0, VolumeUnit.CUBIC_METER)
        delta = VolumeDelta(1, VolumeUnit.CUBIC_METER)
        new_volume_left_add = volume + delta
        new_volume_right_add = delta + volume
        self.assertIsInstance(new_volume_left_add, Volume)
        self.assertAlmostEqual(1, new_volume_left_add.as_unit(VolumeUnit.CUBIC_METER))
        self.assertIsInstance(new_volume_right_add, Volume)
        self.assertAlmostEqual(1, new_volume_right_add.as_unit(VolumeUnit.CUBIC_METER))

    def test_subtract_volume_delta_from_volume_produces_Volume(
        self,
    ) -> None:
        volume = Volume(1, VolumeUnit.CUBIC_METER)
        delta = VolumeDelta(1, VolumeUnit.CUBIC_METER)
        new_volume = volume - delta
        self.assertIsInstance(new_volume, Volume)
        self.assertAlmostEqual(0, new_volume.as_unit(VolumeUnit.CUBIC_METER))

    def test_subtract_volume_from_volume_produces_volume_delta(
        self,
    ) -> None:
        volume1 = Volume(3, VolumeUnit.CUBIC_METER)
        volume2 = Volume(2, VolumeUnit.CUBIC_METER)
        new_volume_delta = volume1 - volume2
        self.assertIsInstance(new_volume_delta, VolumeDelta)
        self.assertAlmostEqual(1, new_volume_delta.as_unit(VolumeUnit.CUBIC_METER))
