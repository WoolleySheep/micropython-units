import unittest

from src.units import AreaDelta, AreaUnit


class AreaDeltaTest(unittest.TestCase):
    """Unit tests for area delta class."""

    def test_create_area_delta(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = AreaDelta(1, AreaUnit.SQUARE_METRE)

    def test_get_area_delta_value_as_unit(self) -> None:
        delta = AreaDelta(1, AreaUnit.SQUARE_METRE)

        for unit, expected_value in [
            (AreaUnit.SQUARE_METRE, 1),
            (AreaUnit.SQUARE_CENTIMETRE, 1e4),
            (AreaUnit.SQUARE_MILLIMETRE, 1e6),
            (AreaUnit.SQUARE_YARD, 1.09361329834**2),
            (AreaUnit.SQUARE_FOOT, 3.28083989501**2),
            (AreaUnit.SQUARE_INCH, 39.3700787402**2),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, delta.as_unit(unit))

    def test_add_area_deltas_produces_area_delta(self) -> None:
        delta1 = AreaDelta(1, AreaUnit.SQUARE_METRE)
        delta2 = AreaDelta(2, AreaUnit.SQUARE_METRE)
        new_delta = delta1 + delta2
        self.assertAlmostEqual(3, new_delta.as_unit(AreaUnit.SQUARE_METRE))

    def test_subtract_area_deltas_produces_area_delta(self) -> None:
        delta1 = AreaDelta(3, AreaUnit.SQUARE_METRE)
        delta2 = AreaDelta(2, AreaUnit.SQUARE_METRE)
        new_delta = delta1 - delta2
        self.assertAlmostEqual(1, new_delta.as_unit(AreaUnit.SQUARE_METRE))

    def test_multiply_area_delta_by_value(self) -> None:
        delta = AreaDelta(1, AreaUnit.SQUARE_METRE)
        new_delta_left_mult = 2 * delta
        new_delta_right_mult = delta * 2
        self.assertAlmostEqual(2, new_delta_left_mult.as_unit(AreaUnit.SQUARE_METRE))
        self.assertAlmostEqual(2, new_delta_right_mult.as_unit(AreaUnit.SQUARE_METRE))

    def test_divide_area_delta_by_value(self) -> None:
        delta = AreaDelta(2, AreaUnit.SQUARE_METRE)
        new_delta = delta / 2
        self.assertAlmostEqual(1, new_delta.as_unit(AreaUnit.SQUARE_METRE))

    def test_divide_area_delta_by_area_delta_produces_ratio(self) -> None:
        delta1 = AreaDelta(2, AreaUnit.SQUARE_METRE)
        delta2 = AreaDelta(1, AreaUnit.SQUARE_METRE)
        ratio = delta1 / delta2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_area_delta(self) -> None:
        delta = AreaDelta(1, AreaUnit.SQUARE_METRE)
        new_delta = -delta
        self.assertAlmostEqual(-1, new_delta.as_unit(AreaUnit.SQUARE_METRE))

    def test_absolute_of_area_delta(self) -> None:
        delta = AreaDelta(-1, AreaUnit.SQUARE_METRE)
        new_delta = abs(delta)
        self.assertAlmostEqual(1, new_delta.as_unit(AreaUnit.SQUARE_METRE))

    def test_floor_divide_area_delta_by_area_delta_produces_floored_ratio(
        self,
    ) -> None:
        delta1 = AreaDelta(3, AreaUnit.SQUARE_METRE)
        delta2 = AreaDelta(2, AreaUnit.SQUARE_METRE)
        floored_ratio = delta1 // delta2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_area_delta_by_area_delta_produces_ratio_remainder(
        self,
    ) -> None:
        delta1 = AreaDelta(3, AreaUnit.SQUARE_METRE)
        delta2 = AreaDelta(2, AreaUnit.SQUARE_METRE)
        remainder = delta1 % delta2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_area_delta_by_area_delta_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        delta1 = AreaDelta(3, AreaUnit.SQUARE_METRE)
        delta2 = AreaDelta(2, AreaUnit.SQUARE_METRE)
        floored_ratio, remainder = divmod(delta1, delta2)
        self.assertAlmostEqual(1, floored_ratio)
        self.assertAlmostEqual(1, remainder)

    def test_compare_area_deltas(self) -> None:
        for (
            area_delta1,
            area_delta2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                AreaDelta(0, AreaUnit.SQUARE_METRE),
                AreaDelta(0, AreaUnit.SQUARE_METRE),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                AreaDelta(0, AreaUnit.SQUARE_METRE),
                AreaDelta(1, AreaUnit.SQUARE_METRE),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                AreaDelta(1, AreaUnit.SQUARE_METRE),
                AreaDelta(0, AreaUnit.SQUARE_METRE),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                area_delta1=area_delta1,
                area_delta2=area_delta2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, area_delta1 == area_delta2)
                self.assertEqual(is_not_equal, area_delta1 != area_delta2)
                self.assertEqual(is_less_than, area_delta1 < area_delta2)
                self.assertEqual(is_less_than_or_equal_to, area_delta1 <= area_delta2)
                self.assertEqual(is_greater_than, area_delta1 > area_delta2)
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    area_delta1 >= area_delta2,
                )
