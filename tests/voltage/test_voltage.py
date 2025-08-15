import unittest

from units import Voltage, VoltageUnit


class VoltageTest(unittest.TestCase):
    """Unit tests for voltage class."""

    def test_create_voltage(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Voltage(1, VoltageUnit.VOLT)

    def test_get_voltage_value_as_unit(self) -> None:
        voltage = Voltage(1, VoltageUnit.VOLT)

        for unit, expected_value in [
            (VoltageUnit.VOLT, 1),
            (VoltageUnit.MILLIVOLT, 1_000),
            (VoltageUnit.MICROVOLT, 1_000_000),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, voltage.as_unit(unit))

    def test_add_voltages_produces_voltage(self) -> None:
        voltage1 = Voltage(1, VoltageUnit.VOLT)
        voltage2 = Voltage(2, VoltageUnit.VOLT)
        new_voltage = voltage1 + voltage2
        self.assertAlmostEqual(3, new_voltage.as_unit(VoltageUnit.VOLT))

    def test_subtract_voltages_produces_voltage(self) -> None:
        voltage1 = Voltage(3, VoltageUnit.VOLT)
        voltage2 = Voltage(2, VoltageUnit.VOLT)
        new_voltage = voltage1 - voltage2
        self.assertAlmostEqual(1, new_voltage.as_unit(VoltageUnit.VOLT))

    def test_multiply_voltage_by_value(self) -> None:
        voltage = Voltage(1, VoltageUnit.VOLT)
        new_voltage_left_mult = 2 * voltage
        new_voltage_right_mult = voltage * 2
        self.assertAlmostEqual(2, new_voltage_left_mult.as_unit(VoltageUnit.VOLT))
        self.assertAlmostEqual(2, new_voltage_right_mult.as_unit(VoltageUnit.VOLT))

    def test_divide_voltage_by_value(self) -> None:
        voltage = Voltage(2, VoltageUnit.VOLT)
        new_voltage = voltage / 2
        self.assertAlmostEqual(1, new_voltage.as_unit(VoltageUnit.VOLT))

    def test_divide_voltage_by_voltage_produces_ratio(self) -> None:
        voltage1 = Voltage(2, VoltageUnit.VOLT)
        voltage2 = Voltage(1, VoltageUnit.VOLT)
        ratio = voltage1 / voltage2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_voltage(self) -> None:
        voltage = Voltage(1, VoltageUnit.VOLT)
        new_voltage = -voltage
        self.assertAlmostEqual(-1, new_voltage.as_unit(VoltageUnit.VOLT))

    def test_absolute_of_voltage(self) -> None:
        voltage = Voltage(-1, VoltageUnit.VOLT)
        new_voltage = abs(voltage)
        self.assertAlmostEqual(1, new_voltage.as_unit(VoltageUnit.VOLT))

    def test_floor_divide_voltage_by_voltage_produces_floored_ratio(
        self,
    ) -> None:
        voltage1 = Voltage(3, VoltageUnit.VOLT)
        voltage2 = Voltage(2, VoltageUnit.VOLT)
        floored_ratio = voltage1 // voltage2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_voltage_by_voltage_produces_ratio_remainder(
        self,
    ) -> None:
        voltage1 = Voltage(3, VoltageUnit.VOLT)
        voltage2 = Voltage(2, VoltageUnit.VOLT)
        remainder = voltage1 % voltage2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_voltage_by_voltage_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        voltage1 = Voltage(3, VoltageUnit.VOLT)
        voltage2 = Voltage(2, VoltageUnit.VOLT)
        floored_ratio, remainder = divmod(voltage1, voltage2)
        self.assertAlmostEqual(1, floored_ratio)
        self.assertAlmostEqual(1, remainder)

    def test_compare_voltages(self) -> None:
        for (
            voltage1,
            voltage2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                Voltage(0, VoltageUnit.VOLT),
                Voltage(0, VoltageUnit.VOLT),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                Voltage(0, VoltageUnit.VOLT),
                Voltage(1, VoltageUnit.VOLT),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                Voltage(1, VoltageUnit.VOLT),
                Voltage(0, VoltageUnit.VOLT),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                voltage1=voltage1,
                voltage2=voltage2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, voltage1 == voltage2)
                self.assertEqual(is_not_equal, voltage1 != voltage2)
                self.assertEqual(is_less_than, voltage1 < voltage2)
                self.assertEqual(is_less_than_or_equal_to, voltage1 <= voltage2)
                self.assertEqual(is_greater_than, voltage1 > voltage2)
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    voltage1 >= voltage2,
                )
