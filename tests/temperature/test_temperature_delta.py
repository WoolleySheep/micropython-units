import unittest

from units import TemperatureDelta, TemperatureUnit


class TemperatureDeltaTest(unittest.TestCase):
    """Unit tests for temperature delta class."""

    def test_create_temperature_delta(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = TemperatureDelta(1, TemperatureUnit.CELSIUS)

    def test_get_temperature_delta_value_as_unit(self) -> None:
        delta = TemperatureDelta(1, TemperatureUnit.CELSIUS)

        for unit, expected_value in [
            (TemperatureUnit.CELSIUS, 1.0),
            (TemperatureUnit.KELVIN, 1.0),
            (TemperatureUnit.FAHRENHEIT, 9 / 5),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, delta.as_unit(unit))

    def test_add_temperature_deltas_produces_temperature_delta(self) -> None:
        delta1 = TemperatureDelta(1, TemperatureUnit.CELSIUS)
        delta2 = TemperatureDelta(2, TemperatureUnit.CELSIUS)
        new_delta = delta1 + delta2
        self.assertAlmostEqual(3, new_delta.as_unit(TemperatureUnit.CELSIUS))

    def test_subtract_temperature_deltas_produces_temperature_delta(self) -> None:
        delta1 = TemperatureDelta(3, TemperatureUnit.CELSIUS)
        delta2 = TemperatureDelta(2, TemperatureUnit.CELSIUS)
        new_delta = delta1 - delta2
        self.assertAlmostEqual(1, new_delta.as_unit(TemperatureUnit.CELSIUS))

    def test_multiply_temperature_delta_by_value(self) -> None:
        delta = TemperatureDelta(1, TemperatureUnit.CELSIUS)
        new_delta_left_mult = 2 * delta
        new_delta_right_mult = delta * 2
        self.assertAlmostEqual(2, new_delta_left_mult.as_unit(TemperatureUnit.CELSIUS))
        self.assertAlmostEqual(2, new_delta_right_mult.as_unit(TemperatureUnit.CELSIUS))

    def test_divide_temperature_delta_by_value(self) -> None:
        delta = TemperatureDelta(2, TemperatureUnit.CELSIUS)
        new_delta = delta / 2
        self.assertAlmostEqual(1, new_delta.as_unit(TemperatureUnit.CELSIUS))

    def test_divide_temperature_delta_by_temperature_delta_produces_ratio(self) -> None:
        delta1 = TemperatureDelta(2, TemperatureUnit.CELSIUS)
        delta2 = TemperatureDelta(1, TemperatureUnit.CELSIUS)
        ratio = delta1 / delta2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_temperature_delta(self) -> None:
        delta = TemperatureDelta(1, TemperatureUnit.CELSIUS)
        new_delta = -delta
        self.assertAlmostEqual(-1, new_delta.as_unit(TemperatureUnit.CELSIUS))

    def test_absolute_of_temperature_delta(self) -> None:
        delta = TemperatureDelta(-1, TemperatureUnit.CELSIUS)
        new_delta = abs(delta)
        self.assertAlmostEqual(1, new_delta.as_unit(TemperatureUnit.CELSIUS))

    def test_compare_temperature_deltas(self) -> None:
        for (
            temperature_delta1,
            temperature_delta2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                TemperatureDelta(0, TemperatureUnit.CELSIUS),
                TemperatureDelta(0, TemperatureUnit.CELSIUS),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                TemperatureDelta(0, TemperatureUnit.CELSIUS),
                TemperatureDelta(1, TemperatureUnit.CELSIUS),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                TemperatureDelta(1, TemperatureUnit.CELSIUS),
                TemperatureDelta(0, TemperatureUnit.CELSIUS),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                temperature_delta1=temperature_delta1,
                temperature_delta2=temperature_delta2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, temperature_delta1 == temperature_delta2)
                self.assertEqual(is_not_equal, temperature_delta1 != temperature_delta2)
                self.assertEqual(is_less_than, temperature_delta1 < temperature_delta2)
                self.assertEqual(
                    is_less_than_or_equal_to, temperature_delta1 <= temperature_delta2
                )
                self.assertEqual(
                    is_greater_than, temperature_delta1 > temperature_delta2
                )
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    temperature_delta1 >= temperature_delta2,
                )
