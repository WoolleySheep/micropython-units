import unittest

from src.units import Mass, MassUnit, NegativeMassValueError


class MassTest(unittest.TestCase):
    """Unit tests for mass class."""

    def test_create_mass(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Mass(1, MassUnit.KILOGRAM)

    def test_exception_raised_when_creating_mass_value_is_negative(
        self,
    ) -> None:
        with self.assertRaises(NegativeMassValueError) as cm:
            _ = Mass(-300, MassUnit.KILOGRAM)
        self.assertAlmostEqual(-300, cm.exception.value)

    def test_get_mass_value_as_unit(self) -> None:
        mass = Mass(1, MassUnit.KILOGRAM)

        for unit, expected_value in [
            (MassUnit.KILOGRAM, 1),
            (MassUnit.GRAM, 1_000),
            (MassUnit.MILLIGRAM, 1_000_000),
            (MassUnit.POUND, 2.20462262185),
            (MassUnit.OUNCE, 35.2739619496),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, mass.as_unit(unit))

    def test_compare_masss(self) -> None:
        for (
            mass1,
            mass2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                Mass(0, MassUnit.KILOGRAM),
                Mass(0, MassUnit.KILOGRAM),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                Mass(0, MassUnit.KILOGRAM),
                Mass(1, MassUnit.KILOGRAM),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                Mass(1, MassUnit.KILOGRAM),
                Mass(0, MassUnit.KILOGRAM),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                mass1=mass1,
                mass2=mass2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, mass1 == mass2)
                self.assertEqual(is_not_equal, mass1 != mass2)
                self.assertEqual(is_less_than, mass1 < mass2)
                self.assertEqual(is_less_than_or_equal_to, mass1 <= mass2)
                self.assertEqual(is_greater_than, mass1 > mass2)
                self.assertEqual(is_greater_than_or_equal_to, mass1 >= mass2)
