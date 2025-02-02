import unittest

from units import NegativeVolumeValueError, Volume, VolumeUnit


class VolumeTest(unittest.TestCase):
    """Unit tests for volume class."""

    def test_create_volume(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Volume(1, VolumeUnit.CUBIC_METER)

    def test_exception_raised_when_creating_volume_value_is_negative(
        self,
    ) -> None:
        with self.assertRaises(NegativeVolumeValueError) as cm:
            _ = Volume(-300, VolumeUnit.CUBIC_METER)
        self.assertAlmostEqual(-300, cm.exception.value)

    def test_get_volume_value_as_unit(self) -> None:
        volume = Volume(1, VolumeUnit.CUBIC_METER)

        for unit, expected_value in [
            (VolumeUnit.CUBIC_METER, 1),
            (VolumeUnit.LITRE, 1_000),
            (VolumeUnit.MILLILITRE, 1_000_000),
            (VolumeUnit.MICROLITRE, 1_000_000_000),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, volume.as_unit(unit))

    def test_compare_volumes(self) -> None:
        for (
            volume1,
            volume2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                Volume(0, VolumeUnit.CUBIC_METER),
                Volume(0, VolumeUnit.CUBIC_METER),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                Volume(0, VolumeUnit.CUBIC_METER),
                Volume(1, VolumeUnit.CUBIC_METER),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                Volume(1, VolumeUnit.CUBIC_METER),
                Volume(0, VolumeUnit.CUBIC_METER),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                volume1=volume1,
                volume2=volume2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, volume1 == volume2)
                self.assertEqual(is_not_equal, volume1 != volume2)
                self.assertEqual(is_less_than, volume1 < volume2)
                self.assertEqual(is_less_than_or_equal_to, volume1 <= volume2)
                self.assertEqual(is_greater_than, volume1 > volume2)
                self.assertEqual(is_greater_than_or_equal_to, volume1 >= volume2)
