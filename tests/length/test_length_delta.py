import unittest

from src.units import DistanceUnit, LengthDelta


class LengthDeltaTest(unittest.TestCase):
    """Unit tests for length delta class."""

    def test_create_length_delta(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = LengthDelta(1, DistanceUnit.METRE)

    def test_get_length_delta_value_as_unit(self) -> None:
        delta = LengthDelta(1, DistanceUnit.METRE)

        for unit, expected_value in [
            (DistanceUnit.METRE, 1),
            (DistanceUnit.CENTIMETRE, 100),
            (DistanceUnit.MILLIMETRE, 1_000),
            (DistanceUnit.YARD, 1.09361329834),
            (DistanceUnit.FOOT, 3.28083989501),
            (DistanceUnit.INCH, 39.3700787402),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, delta.as_unit(unit))

    def test_add_length_deltas_produces_length_delta(self) -> None:
        delta1 = LengthDelta(1, DistanceUnit.METRE)
        delta2 = LengthDelta(2, DistanceUnit.METRE)
        new_delta = delta1 + delta2
        self.assertAlmostEqual(3, new_delta.as_unit(DistanceUnit.METRE))

    def test_subtract_length_deltas_produces_length_delta(self) -> None:
        delta1 = LengthDelta(3, DistanceUnit.METRE)
        delta2 = LengthDelta(2, DistanceUnit.METRE)
        new_delta = delta1 - delta2
        self.assertAlmostEqual(1, new_delta.as_unit(DistanceUnit.METRE))

    def test_multiply_length_delta_by_value(self) -> None:
        delta = LengthDelta(1, DistanceUnit.METRE)
        new_delta_left_mult = 2 * delta
        new_delta_right_mult = delta * 2
        self.assertAlmostEqual(2, new_delta_left_mult.as_unit(DistanceUnit.METRE))
        self.assertAlmostEqual(2, new_delta_right_mult.as_unit(DistanceUnit.METRE))

    def test_divide_length_delta_by_value(self) -> None:
        delta = LengthDelta(2, DistanceUnit.METRE)
        new_delta = delta / 2
        self.assertAlmostEqual(1, new_delta.as_unit(DistanceUnit.METRE))

    def test_divide_length_delta_by_length_delta_produces_ratio(self) -> None:
        delta1 = LengthDelta(2, DistanceUnit.METRE)
        delta2 = LengthDelta(1, DistanceUnit.METRE)
        ratio = delta1 / delta2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_length_delta(self) -> None:
        delta = LengthDelta(1, DistanceUnit.METRE)
        new_delta = -delta
        self.assertAlmostEqual(-1, new_delta.as_unit(DistanceUnit.METRE))

    def test_absolute_of_length_delta(self) -> None:
        delta = LengthDelta(-1, DistanceUnit.METRE)
        new_delta = abs(delta)
        self.assertAlmostEqual(1, new_delta.as_unit(DistanceUnit.METRE))

    def test_floor_divide_length_delta_by_length_delta_produces_floored_ratio(
        self,
    ) -> None:
        delta1 = LengthDelta(3, DistanceUnit.METRE)
        delta2 = LengthDelta(2, DistanceUnit.METRE)
        floored_ratio = delta1 // delta2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_length_delta_by_length_delta_produces_ratio_remainder(
        self,
    ) -> None:
        delta1 = LengthDelta(3, DistanceUnit.METRE)
        delta2 = LengthDelta(2, DistanceUnit.METRE)
        remainder = delta1 % delta2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_length_delta_by_length_delta_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        delta1 = LengthDelta(3, DistanceUnit.METRE)
        delta2 = LengthDelta(2, DistanceUnit.METRE)
        floored_ratio, remainder = divmod(delta1, delta2)
        self.assertAlmostEqual(1, floored_ratio)
        self.assertAlmostEqual(1, remainder)

    def test_compare_length_deltas(self) -> None:
        for (
            length_delta1,
            length_delta2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                LengthDelta(0, DistanceUnit.METRE),
                LengthDelta(0, DistanceUnit.METRE),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                LengthDelta(0, DistanceUnit.METRE),
                LengthDelta(1, DistanceUnit.METRE),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                LengthDelta(1, DistanceUnit.METRE),
                LengthDelta(0, DistanceUnit.METRE),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                length_delta1=length_delta1,
                length_delta2=length_delta2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, length_delta1 == length_delta2)
                self.assertEqual(is_not_equal, length_delta1 != length_delta2)
                self.assertEqual(is_less_than, length_delta1 < length_delta2)
                self.assertEqual(
                    is_less_than_or_equal_to, length_delta1 <= length_delta2
                )
                self.assertEqual(is_greater_than, length_delta1 > length_delta2)
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    length_delta1 >= length_delta2,
                )
