import unittest

from src.units import (
    TimeUnit,
    VolumetricFlowRate,
    VolumeUnit,
)


class VolumetricFlowRateTest(unittest.TestCase):
    """Unit tests for volumetric flow rate class."""

    def test_create_flow_rate(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = VolumetricFlowRate(1, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)

    def test_get_flow_rate_value_as_unit(self) -> None:
        delta = VolumetricFlowRate(1, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)

        for volume_unit, time_unit, expected_value in [
            (VolumeUnit.CUBIC_METRE, TimeUnit.SECOND, 1),
            (VolumeUnit.LITRE, TimeUnit.SECOND, 1e3),
            (VolumeUnit.MILLILITRE, TimeUnit.SECOND, 1e6),
            (VolumeUnit.MICROLITRE, TimeUnit.SECOND, 1e9),
            (VolumeUnit.CUBIC_METRE, TimeUnit.MINUTE, 60),
            (VolumeUnit.LITRE, TimeUnit.MINUTE, 60 * 1e3),
            (VolumeUnit.MILLILITRE, TimeUnit.MINUTE, 60 * 1e6),
            (VolumeUnit.MICROLITRE, TimeUnit.MINUTE, 60 * 1e9),
            (VolumeUnit.CUBIC_METRE, TimeUnit.HOUR, 60 * 60),
            (VolumeUnit.LITRE, TimeUnit.HOUR, 60 * 60 * 1e3),
            (VolumeUnit.MILLILITRE, TimeUnit.HOUR, 60 * 60 * 1e6),
            (VolumeUnit.MICROLITRE, TimeUnit.HOUR, 60 * 60 * 1e9),
            (VolumeUnit.CUBIC_METRE, TimeUnit.MICROSECOND, 1e-6),
            (VolumeUnit.LITRE, TimeUnit.MICROSECOND, 1e-3),
            (VolumeUnit.MILLILITRE, TimeUnit.MICROSECOND, 1),
            (VolumeUnit.MICROLITRE, TimeUnit.MICROSECOND, 1e3),
            (VolumeUnit.CUBIC_METRE, TimeUnit.MILLISECOND, 1e-3),
            (VolumeUnit.LITRE, TimeUnit.MILLISECOND, 1),
            (VolumeUnit.MILLILITRE, TimeUnit.MILLISECOND, 1e3),
            (VolumeUnit.MICROLITRE, TimeUnit.MILLISECOND, 1e6),
        ]:
            with self.subTest(unit=volume_unit, expected_value=expected_value):
                self.assertAlmostEqual(
                    expected_value, delta.as_unit(volume_unit, time_unit)
                )

    def test_add_flow_rates_produces_flow_rate(self) -> None:
        flow_rate1 = VolumetricFlowRate(1, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        flow_rate2 = VolumetricFlowRate(2, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        new_flow_rate = flow_rate1 + flow_rate2
        self.assertAlmostEqual(
            3, new_flow_rate.as_unit(VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        )

    def test_subtract_flow_rates_produces_flow_rate(self) -> None:
        flow_rate1 = VolumetricFlowRate(3, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        flow_rate2 = VolumetricFlowRate(2, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        new_flow_rate = flow_rate1 - flow_rate2
        self.assertAlmostEqual(
            1, new_flow_rate.as_unit(VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        )

    def test_multiply_flow_rate_by_value(self) -> None:
        flow_rate = VolumetricFlowRate(1, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        new_flow_rate_left_mult = 2 * flow_rate
        new_flow_rate_right_mult = flow_rate * 2
        self.assertAlmostEqual(
            2, new_flow_rate_left_mult.as_unit(VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        )
        self.assertAlmostEqual(
            2, new_flow_rate_right_mult.as_unit(VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        )

    def test_divide_flow_rate_by_value(self) -> None:
        flow_rate = VolumetricFlowRate(2, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        new_flow_rate = flow_rate / 2
        self.assertAlmostEqual(
            1, new_flow_rate.as_unit(VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        )

    def test_divide_flow_rate_by_flow_rate_produces_ratio(self) -> None:
        flow_rate1 = VolumetricFlowRate(2, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        flow_rate2 = VolumetricFlowRate(1, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        ratio = flow_rate1 / flow_rate2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_flow_rate(self) -> None:
        flow_rate = VolumetricFlowRate(1, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        negative_flow_rate = -flow_rate
        self.assertAlmostEqual(
            -1, negative_flow_rate.as_unit(VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        )

    def test_absolute_of_flow_rate(self) -> None:
        flow_rate = VolumetricFlowRate(-1, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        absolute_flow_rate = abs(flow_rate)
        self.assertAlmostEqual(
            1, absolute_flow_rate.as_unit(VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        )

    def test_floor_divide_flow_rate_by_flow_rate_produces_floored_ratio(
        self,
    ) -> None:
        flow_rate1 = VolumetricFlowRate(3, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        flow_rate2 = VolumetricFlowRate(2, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        floored_ratio = flow_rate1 // flow_rate2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_flow_rate_by_flow_rate_produces_ratio_remainder(
        self,
    ) -> None:
        flow_rate1 = VolumetricFlowRate(3, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        flow_rate2 = VolumetricFlowRate(2, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        remainder = flow_rate1 % flow_rate2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_flow_rate_by_flow_rate_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        flow_rate1 = VolumetricFlowRate(3, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        flow_rate2 = VolumetricFlowRate(2, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND)
        floored_ratio, remainder = divmod(flow_rate1, flow_rate2)
        self.assertAlmostEqual(1, floored_ratio)
        self.assertAlmostEqual(1, remainder)

    def test_compare_flow_rates(self) -> None:
        for (
            flow_rate1,
            flow_rate2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                VolumetricFlowRate(0, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND),
                VolumetricFlowRate(0, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                VolumetricFlowRate(0, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND),
                VolumetricFlowRate(1, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                VolumetricFlowRate(1, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND),
                VolumetricFlowRate(0, VolumeUnit.CUBIC_METRE, TimeUnit.SECOND),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                volume_delta1=flow_rate1,
                volume_delta2=flow_rate2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, flow_rate1 == flow_rate2)
                self.assertEqual(is_not_equal, flow_rate1 != flow_rate2)
                self.assertEqual(is_less_than, flow_rate1 < flow_rate2)
                self.assertEqual(is_less_than_or_equal_to, flow_rate1 <= flow_rate2)
                self.assertEqual(is_greater_than, flow_rate1 > flow_rate2)
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    flow_rate1 >= flow_rate2,
                )
