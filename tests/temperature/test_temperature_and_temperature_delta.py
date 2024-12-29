import unittest

from units import Temperature, TemperatureDelta, TemperatureUnit


class TemperatureAndTemperatureDeltaTest(unittest.TestCase):
    """Unit tests for interactions between temperature and temperature delta classes."""

    def test_add_temperature_delta_to_temperature_produces_temperature(self) -> None:
        temperature = Temperature(0, TemperatureUnit.CELSIUS)
        delta = TemperatureDelta(1, TemperatureUnit.CELSIUS)
        new_temperature_left_add = temperature + delta
        new_temperature_right_add = delta + temperature
        self.assertIsInstance(new_temperature_left_add, Temperature)
        self.assertAlmostEqual(
            1, new_temperature_left_add.as_unit(TemperatureUnit.CELSIUS)
        )
        self.assertIsInstance(new_temperature_right_add, Temperature)
        self.assertAlmostEqual(
            1, new_temperature_right_add.as_unit(TemperatureUnit.CELSIUS)
        )

    def test_subtract_temperature_delta_from_temperature_produces_temperature(
        self,
    ) -> None:
        temperature = Temperature(1, TemperatureUnit.CELSIUS)
        delta = TemperatureDelta(1, TemperatureUnit.CELSIUS)
        new_temperature = temperature - delta
        self.assertIsInstance(new_temperature, Temperature)
        self.assertAlmostEqual(0, new_temperature.as_unit(TemperatureUnit.CELSIUS))

    def test_subtract_temperature_from_temperature_produces_temperature_delta(
        self,
    ) -> None:
        temperature1 = Temperature(3, TemperatureUnit.CELSIUS)
        temperature2 = Temperature(2, TemperatureUnit.CELSIUS)
        new_temperature_delta = temperature1 - temperature2
        self.assertIsInstance(new_temperature_delta, TemperatureDelta)
        self.assertAlmostEqual(
            1, new_temperature_delta.as_unit(TemperatureUnit.CELSIUS)
        )
