import unittest

from units import Temperature, TemperatureUnit


class TemperatureTest(unittest.TestCase):
    """Unit tests for temperature class."""

    def test_create_temperature(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Temperature(1, TemperatureUnit.CELSIUS)

    def test_exception_raised_when_creating_temperature_less_than_absolute_zero(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            _ = Temperature(-300, TemperatureUnit.CELSIUS)

    def test_get_temperature_value_as_unit(self) -> None:
        temperature = Temperature(0, TemperatureUnit.CELSIUS)

        # Add subtests for units as they're added here
        for unit, expected_value in [
            (TemperatureUnit.CELSIUS, 0),
            (TemperatureUnit.KELVIN, 273.15),
            (TemperatureUnit.FAHRENHEIT, 32),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, temperature.as_unit(unit))

    def test_compare_temperatures(self) -> None:
        for (
            temperature1,
            temperature2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                Temperature(0, TemperatureUnit.CELSIUS),
                Temperature(0, TemperatureUnit.CELSIUS),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                Temperature(0, TemperatureUnit.CELSIUS),
                Temperature(1, TemperatureUnit.CELSIUS),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                Temperature(1, TemperatureUnit.CELSIUS),
                Temperature(0, TemperatureUnit.CELSIUS),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                temperature1=temperature1,
                temperature2=temperature2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, temperature1 == temperature2)
                self.assertEqual(is_not_equal, temperature1 != temperature2)
                self.assertEqual(is_less_than, temperature1 < temperature2)
                self.assertEqual(is_less_than_or_equal_to, temperature1 <= temperature2)
                self.assertEqual(is_greater_than, temperature1 > temperature2)
                self.assertEqual(
                    is_greater_than_or_equal_to, temperature1 >= temperature2
                )
