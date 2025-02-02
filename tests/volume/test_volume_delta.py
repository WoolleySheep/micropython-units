import unittest

from units import VolumeDelta, VolumeUnit


class VolumeDeltaTest(unittest.TestCase):
    """Unit tests for volume delta class."""

    def test_create_volume_delta(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = VolumeDelta(1, VolumeUnit.CUBIC_METER)

    def test_get_volume_delta_value_as_unit(self) -> None:
        delta = VolumeDelta(1, VolumeUnit.CUBIC_METER)

        for unit, expected_value in [
            (VolumeUnit.CUBIC_METER, 1),
            (VolumeUnit.LITRE, 1_000),
            (VolumeUnit.MILLILITRE, 1_000_000),
            (VolumeUnit.MICROLITRE, 1_000_000_000),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, delta.as_unit(unit))

    def test_add_volume_deltas_produces_volume_delta(self) -> None:
        delta1 = VolumeDelta(1, VolumeUnit.CUBIC_METER)
        delta2 = VolumeDelta(2, VolumeUnit.CUBIC_METER)
        new_delta = delta1 + delta2
        self.assertAlmostEqual(3, new_delta.as_unit(VolumeUnit.CUBIC_METER))

    def test_subtract_volume_deltas_produces_volume_delta(self) -> None:
        delta1 = VolumeDelta(3, VolumeUnit.CUBIC_METER)
        delta2 = VolumeDelta(2, VolumeUnit.CUBIC_METER)
        new_delta = delta1 - delta2
        self.assertAlmostEqual(1, new_delta.as_unit(VolumeUnit.CUBIC_METER))

    def test_multiply_volume_delta_by_value(self) -> None:
        delta = VolumeDelta(1, VolumeUnit.CUBIC_METER)
        new_delta_left_mult = 2 * delta
        new_delta_right_mult = delta * 2
        self.assertAlmostEqual(2, new_delta_left_mult.as_unit(VolumeUnit.CUBIC_METER))
        self.assertAlmostEqual(2, new_delta_right_mult.as_unit(VolumeUnit.CUBIC_METER))

    def test_divide_volume_delta_by_value(self) -> None:
        delta = VolumeDelta(2, VolumeUnit.CUBIC_METER)
        new_delta = delta / 2
        self.assertAlmostEqual(1, new_delta.as_unit(VolumeUnit.CUBIC_METER))

    def test_divide_volume_delta_by_volume_delta_produces_ratio(self) -> None:
        delta1 = VolumeDelta(2, VolumeUnit.CUBIC_METER)
        delta2 = VolumeDelta(1, VolumeUnit.CUBIC_METER)
        ratio = delta1 / delta2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_volume_delta(self) -> None:
        delta = VolumeDelta(1, VolumeUnit.CUBIC_METER)
        new_delta = -delta
        self.assertAlmostEqual(-1, new_delta.as_unit(VolumeUnit.CUBIC_METER))

    def test_absolute_of_volume_delta(self) -> None:
        delta = VolumeDelta(-1, VolumeUnit.CUBIC_METER)
        new_delta = abs(delta)
        self.assertAlmostEqual(1, new_delta.as_unit(VolumeUnit.CUBIC_METER))

    def test_floor_divide_volume_delta_by_volume_delta_produces_floored_ratio(
        self,
    ) -> None:
        delta1 = VolumeDelta(3, VolumeUnit.CUBIC_METER)
        delta2 = VolumeDelta(2, VolumeUnit.CUBIC_METER)
        floored_ratio = delta1 // delta2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_volume_delta_by_volume_delta_produces_ratio_remainder(
        self,
    ) -> None:
        delta1 = VolumeDelta(3, VolumeUnit.CUBIC_METER)
        delta2 = VolumeDelta(2, VolumeUnit.CUBIC_METER)
        remainder = delta1 % delta2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_volume_delta_by_volume_delta_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        delta1 = VolumeDelta(3, VolumeUnit.CUBIC_METER)
        delta2 = VolumeDelta(2, VolumeUnit.CUBIC_METER)
        floored_ratio, remainder = divmod(delta1, delta2)
        self.assertAlmostEqual(1, floored_ratio)
        self.assertAlmostEqual(1, remainder)

    def test_compare_volume_deltas(self) -> None:
        for (
            volume_delta1,
            volume_delta2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                VolumeDelta(0, VolumeUnit.CUBIC_METER),
                VolumeDelta(0, VolumeUnit.CUBIC_METER),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                VolumeDelta(0, VolumeUnit.CUBIC_METER),
                VolumeDelta(1, VolumeUnit.CUBIC_METER),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                VolumeDelta(1, VolumeUnit.CUBIC_METER),
                VolumeDelta(0, VolumeUnit.CUBIC_METER),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                volume_delta1=volume_delta1,
                volume_delta2=volume_delta2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, volume_delta1 == volume_delta2)
                self.assertEqual(is_not_equal, volume_delta1 != volume_delta2)
                self.assertEqual(is_less_than, volume_delta1 < volume_delta2)
                self.assertEqual(
                    is_less_than_or_equal_to, volume_delta1 <= volume_delta2
                )
                self.assertEqual(is_greater_than, volume_delta1 > volume_delta2)
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    volume_delta1 >= volume_delta2,
                )
