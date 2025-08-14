import unittest

from units import (
    MassFlowRate,
    MassUnit,
    TimeUnit,
)


class MassFlowRateTest(unittest.TestCase):
    """Unit tests for mass flow rate class."""

    def test_create_flow_rate(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = MassFlowRate(1, MassUnit.KILOGRAM, TimeUnit.SECOND)

    def test_get_flow_rate_value_as_unit(self) -> None:
        delta = MassFlowRate(1, MassUnit.KILOGRAM, TimeUnit.SECOND)

        for mass_unit, time_unit, expected_value in [
            (MassUnit.KILOGRAM, TimeUnit.SECOND, 1),
            (MassUnit.GRAM, TimeUnit.SECOND, 1e3),
            (MassUnit.MILLIGRAM, TimeUnit.SECOND, 1e6),
            (MassUnit.POUND, TimeUnit.SECOND, 2.20462262185),
            (MassUnit.OUNCE, TimeUnit.SECOND, 35.2739619496),
            (MassUnit.KILOGRAM, TimeUnit.MINUTE, 60),
            (MassUnit.GRAM, TimeUnit.MINUTE, 60 * 1e3),
            (MassUnit.MILLIGRAM, TimeUnit.MINUTE, 60 * 1e6),
            (MassUnit.POUND, TimeUnit.MINUTE, 60 * 2.20462262185),
            (MassUnit.OUNCE, TimeUnit.MINUTE, 60 * 35.2739619496),
            (MassUnit.KILOGRAM, TimeUnit.HOUR, 60 * 60),
            (MassUnit.GRAM, TimeUnit.HOUR, 60 * 60 * 1e3),
            (MassUnit.MILLIGRAM, TimeUnit.HOUR, 60 * 60 * 1e6),
            (MassUnit.POUND, TimeUnit.HOUR, 60 * 60 * 2.20462262185),
            (MassUnit.OUNCE, TimeUnit.HOUR, 60 * 60 * 35.2739619496),
            (MassUnit.KILOGRAM, TimeUnit.MICROSECOND, 1e-6),
            (MassUnit.GRAM, TimeUnit.MICROSECOND, 1e-3),
            (MassUnit.MILLIGRAM, TimeUnit.MICROSECOND, 1),
            (MassUnit.POUND, TimeUnit.MICROSECOND, 2.20462262185 * 1e-6),
            (MassUnit.OUNCE, TimeUnit.MICROSECOND, 35.2739619496 * 1e-6),
            (MassUnit.KILOGRAM, TimeUnit.MILLISECOND, 1e-3),
            (MassUnit.GRAM, TimeUnit.MILLISECOND, 1),
            (MassUnit.MILLIGRAM, TimeUnit.MILLISECOND, 1e3),
            (MassUnit.POUND, TimeUnit.MILLISECOND, 2.20462262185 * 1e-3),
            (MassUnit.OUNCE, TimeUnit.MILLISECOND, 35.2739619496 * 1e-3),
        ]:
            with self.subTest(unit=mass_unit, expected_value=expected_value):
                self.assertAlmostEqual(
                    expected_value, delta.as_unit(mass_unit, time_unit)
                )

    def test_add_flow_rates_produces_flow_rate(self) -> None:
        flow_rate1 = MassFlowRate(1, MassUnit.KILOGRAM, TimeUnit.SECOND)
        flow_rate2 = MassFlowRate(2, MassUnit.KILOGRAM, TimeUnit.SECOND)
        new_flow_rate = flow_rate1 + flow_rate2
        self.assertAlmostEqual(
            3, new_flow_rate.as_unit(MassUnit.KILOGRAM, TimeUnit.SECOND)
        )

    def test_subtract_flow_rates_produces_flow_rate(self) -> None:
        flow_rate1 = MassFlowRate(3, MassUnit.KILOGRAM, TimeUnit.SECOND)
        flow_rate2 = MassFlowRate(2, MassUnit.KILOGRAM, TimeUnit.SECOND)
        new_flow_rate = flow_rate1 - flow_rate2
        self.assertAlmostEqual(
            1, new_flow_rate.as_unit(MassUnit.KILOGRAM, TimeUnit.SECOND)
        )

    def test_multiply_flow_rate_by_value(self) -> None:
        flow_rate = MassFlowRate(1, MassUnit.KILOGRAM, TimeUnit.SECOND)
        new_flow_rate_left_mult = 2 * flow_rate
        new_flow_rate_right_mult = flow_rate * 2
        self.assertAlmostEqual(
            2, new_flow_rate_left_mult.as_unit(MassUnit.KILOGRAM, TimeUnit.SECOND)
        )
        self.assertAlmostEqual(
            2, new_flow_rate_right_mult.as_unit(MassUnit.KILOGRAM, TimeUnit.SECOND)
        )

    def test_divide_flow_rate_by_value(self) -> None:
        flow_rate = MassFlowRate(2, MassUnit.KILOGRAM, TimeUnit.SECOND)
        new_flow_rate = flow_rate / 2
        self.assertAlmostEqual(
            1, new_flow_rate.as_unit(MassUnit.KILOGRAM, TimeUnit.SECOND)
        )

    def test_divide_flow_rate_by_flow_rate_produces_ratio(self) -> None:
        flow_rate1 = MassFlowRate(2, MassUnit.KILOGRAM, TimeUnit.SECOND)
        flow_rate2 = MassFlowRate(1, MassUnit.KILOGRAM, TimeUnit.SECOND)
        ratio = flow_rate1 / flow_rate2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_flow_rate(self) -> None:
        flow_rate = MassFlowRate(1, MassUnit.KILOGRAM, TimeUnit.SECOND)
        negative_flow_rate = -flow_rate
        self.assertAlmostEqual(
            -1, negative_flow_rate.as_unit(MassUnit.KILOGRAM, TimeUnit.SECOND)
        )

    def test_absolute_of_flow_rate(self) -> None:
        flow_rate = MassFlowRate(-1, MassUnit.KILOGRAM, TimeUnit.SECOND)
        absolute_flow_rate = abs(flow_rate)
        self.assertAlmostEqual(
            1, absolute_flow_rate.as_unit(MassUnit.KILOGRAM, TimeUnit.SECOND)
        )

    def test_floor_divide_flow_rate_by_flow_rate_produces_floored_ratio(
        self,
    ) -> None:
        flow_rate1 = MassFlowRate(3, MassUnit.KILOGRAM, TimeUnit.SECOND)
        flow_rate2 = MassFlowRate(2, MassUnit.KILOGRAM, TimeUnit.SECOND)
        floored_ratio = flow_rate1 // flow_rate2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_flow_rate_by_flow_rate_produces_ratio_remainder(
        self,
    ) -> None:
        flow_rate1 = MassFlowRate(3, MassUnit.KILOGRAM, TimeUnit.SECOND)
        flow_rate2 = MassFlowRate(2, MassUnit.KILOGRAM, TimeUnit.SECOND)
        remainder = flow_rate1 % flow_rate2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_flow_rate_by_flow_rate_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        flow_rate1 = MassFlowRate(3, MassUnit.KILOGRAM, TimeUnit.SECOND)
        flow_rate2 = MassFlowRate(2, MassUnit.KILOGRAM, TimeUnit.SECOND)
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
                MassFlowRate(0, MassUnit.KILOGRAM, TimeUnit.SECOND),
                MassFlowRate(0, MassUnit.KILOGRAM, TimeUnit.SECOND),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                MassFlowRate(0, MassUnit.KILOGRAM, TimeUnit.SECOND),
                MassFlowRate(1, MassUnit.KILOGRAM, TimeUnit.SECOND),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                MassFlowRate(1, MassUnit.KILOGRAM, TimeUnit.SECOND),
                MassFlowRate(0, MassUnit.KILOGRAM, TimeUnit.SECOND),
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
