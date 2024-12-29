import unittest

from units import Pressure, PressureDelta, PressureUnit


class PressureAndPressureDeltaTest(unittest.TestCase):
    """Unit tests for interactions between pressure and pressure delta classes."""

    def test_add_pressure_delta_to_pressure_produces_pressure(self) -> None:
        pressure = Pressure(0, PressureUnit.PASCAL)
        delta = PressureDelta(1, PressureUnit.PASCAL)
        new_pressure_left_add = pressure + delta
        new_pressure_right_add = delta + pressure
        self.assertIsInstance(new_pressure_left_add, Pressure)
        self.assertAlmostEqual(1, new_pressure_left_add.as_unit(PressureUnit.PASCAL))
        self.assertIsInstance(new_pressure_right_add, Pressure)
        self.assertAlmostEqual(1, new_pressure_right_add.as_unit(PressureUnit.PASCAL))

    def test_subtract_pressure_delta_from_pressure_produces_pressure(
        self,
    ) -> None:
        pressure = Pressure(1, PressureUnit.PASCAL)
        delta = PressureDelta(1, PressureUnit.PASCAL)
        new_pressure = pressure - delta
        self.assertIsInstance(new_pressure, Pressure)
        self.assertAlmostEqual(0, new_pressure.as_unit(PressureUnit.PASCAL))

    def test_subtract_pressure_from_pressure_produces_pressure_delta(
        self,
    ) -> None:
        pressure1 = Pressure(3, PressureUnit.PASCAL)
        pressure2 = Pressure(2, PressureUnit.PASCAL)
        new_pressure_delta = pressure1 - pressure2
        self.assertIsInstance(new_pressure_delta, PressureDelta)
        self.assertAlmostEqual(1, new_pressure_delta.as_unit(PressureUnit.PASCAL))
