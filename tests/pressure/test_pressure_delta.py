import unittest

from units import PressureDelta, PressureUnit


class PressureDeltaTest(unittest.TestCase):
    """Unit tests for pressure delta class."""

    def test_create_pressure_delta(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = PressureDelta(1, PressureUnit.PASCAL)

    def test_get_pressure_delta_value_as_unit(self) -> None:
        delta = PressureDelta(1, PressureUnit.PASCAL)

        for unit, expected_value in [
            (PressureUnit.PASCAL, 1.0),
            (PressureUnit.POUND_PER_SQUARE_INCH, 0.00014503773773),
            (PressureUnit.BAR, 1 / 100_000),
            (PressureUnit.ATMOSPHERE, 1 / 101_325),
            (PressureUnit.MILLIMETRE_OF_MERCURY, 1 / 133.322387415),
            (PressureUnit.KILOPASCAL, 1 / 1_000),
            (PressureUnit.MILLIBAR, 1 / 100),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, delta.as_unit(unit))

    def test_add_pressure_deltas_produces_pressure_delta(self) -> None:
        delta1 = PressureDelta(1, PressureUnit.PASCAL)
        delta2 = PressureDelta(2, PressureUnit.PASCAL)
        new_delta = delta1 + delta2
        self.assertAlmostEqual(3, new_delta.as_unit(PressureUnit.PASCAL))

    def test_subtract_pressure_deltas_produces_pressure_delta(self) -> None:
        delta1 = PressureDelta(3, PressureUnit.PASCAL)
        delta2 = PressureDelta(2, PressureUnit.PASCAL)
        new_delta = delta1 - delta2
        self.assertAlmostEqual(1, new_delta.as_unit(PressureUnit.PASCAL))

    def test_multiply_pressure_delta_by_value(self) -> None:
        delta = PressureDelta(1, PressureUnit.PASCAL)
        new_delta_left_mult = 2 * delta
        new_delta_right_mult = delta * 2
        self.assertAlmostEqual(2, new_delta_left_mult.as_unit(PressureUnit.PASCAL))
        self.assertAlmostEqual(2, new_delta_right_mult.as_unit(PressureUnit.PASCAL))

    def test_divide_pressure_delta_by_value(self) -> None:
        delta = PressureDelta(2, PressureUnit.PASCAL)
        new_delta = delta / 2
        self.assertAlmostEqual(1, new_delta.as_unit(PressureUnit.PASCAL))

    def test_divide_pressure_delta_by_pressure_delta_produces_ratio(self) -> None:
        delta1 = PressureDelta(2, PressureUnit.PASCAL)
        delta2 = PressureDelta(1, PressureUnit.PASCAL)
        ratio = delta1 / delta2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_pressure_delta(self) -> None:
        delta = PressureDelta(1, PressureUnit.PASCAL)
        new_delta = -delta
        self.assertAlmostEqual(-1, new_delta.as_unit(PressureUnit.PASCAL))

    def test_absolute_of_pressure_delta(self) -> None:
        delta = PressureDelta(-1, PressureUnit.PASCAL)
        new_delta = abs(delta)
        self.assertAlmostEqual(1, new_delta.as_unit(PressureUnit.PASCAL))

    def test_floor_divide_pressure_delta_by_pressure_delta_produces_floored_ratio(
        self,
    ) -> None:
        delta1 = PressureDelta(3, PressureUnit.PASCAL)
        delta2 = PressureDelta(2, PressureUnit.PASCAL)
        floored_ratio = delta1 // delta2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_pressure_delta_by_pressure_delta_produces_ratio_remainder(
        self,
    ) -> None:
        delta1 = PressureDelta(3, PressureUnit.PASCAL)
        delta2 = PressureDelta(2, PressureUnit.PASCAL)
        remainder = delta1 % delta2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_pressure_delta_by_pressure_delta_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        delta1 = PressureDelta(3, PressureUnit.PASCAL)
        delta2 = PressureDelta(2, PressureUnit.PASCAL)
        floored_ratio, remainder = divmod(delta1, delta2)
        self.assertAlmostEqual(1, floored_ratio)
        self.assertAlmostEqual(1, remainder)

    def test_compare_pressure_deltas(self) -> None:
        for (
            pressure_delta1,
            pressure_delta2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                PressureDelta(0, PressureUnit.PASCAL),
                PressureDelta(0, PressureUnit.PASCAL),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                PressureDelta(0, PressureUnit.PASCAL),
                PressureDelta(1, PressureUnit.PASCAL),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                PressureDelta(1, PressureUnit.PASCAL),
                PressureDelta(0, PressureUnit.PASCAL),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                pressure_delta1=pressure_delta1,
                pressure_delta2=pressure_delta2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, pressure_delta1 == pressure_delta2)
                self.assertEqual(is_not_equal, pressure_delta1 != pressure_delta2)
                self.assertEqual(is_less_than, pressure_delta1 < pressure_delta2)
                self.assertEqual(
                    is_less_than_or_equal_to, pressure_delta1 <= pressure_delta2
                )
                self.assertEqual(is_greater_than, pressure_delta1 > pressure_delta2)
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    pressure_delta1 >= pressure_delta2,
                )
