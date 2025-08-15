import unittest

from src.units import NegativePressureValueError, Pressure, PressureUnit


class PressureTest(unittest.TestCase):
    """Unit tests for pressure class."""

    def test_create_pressure(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Pressure(1, PressureUnit.PASCAL)

    def test_exception_raised_when_creating_pressure_value_is_negative(
        self,
    ) -> None:
        with self.assertRaises(NegativePressureValueError) as cm:
            _ = Pressure(-300, PressureUnit.PASCAL)
        self.assertAlmostEqual(-300, cm.exception.value)

    def test_get_pressure_value_as_unit(self) -> None:
        pressure = Pressure(1, PressureUnit.PASCAL)

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
                self.assertAlmostEqual(expected_value, pressure.as_unit(unit))

    def test_compare_pressures(self) -> None:
        for (
            pressure1,
            pressure2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                Pressure(0, PressureUnit.PASCAL),
                Pressure(0, PressureUnit.PASCAL),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                Pressure(0, PressureUnit.PASCAL),
                Pressure(1, PressureUnit.PASCAL),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                Pressure(1, PressureUnit.PASCAL),
                Pressure(0, PressureUnit.PASCAL),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                pressure1=pressure1,
                pressure2=pressure2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, pressure1 == pressure2)
                self.assertEqual(is_not_equal, pressure1 != pressure2)
                self.assertEqual(is_less_than, pressure1 < pressure2)
                self.assertEqual(is_less_than_or_equal_to, pressure1 <= pressure2)
                self.assertEqual(is_greater_than, pressure1 > pressure2)
                self.assertEqual(is_greater_than_or_equal_to, pressure1 >= pressure2)
