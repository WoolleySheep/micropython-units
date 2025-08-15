import unittest

from src.units import MassDelta, MassUnit


class MassDeltaTest(unittest.TestCase):
    """Unit tests for mass delta class."""

    def test_create_mass_delta(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = MassDelta(1, MassUnit.KILOGRAM)

    def test_get_mass_delta_value_as_unit(self) -> None:
        delta = MassDelta(1, MassUnit.KILOGRAM)

        for unit, expected_value in [
            (MassUnit.KILOGRAM, 1),
            (MassUnit.GRAM, 1_000),
            (MassUnit.MILLIGRAM, 1_000_000),
            (MassUnit.POUND, 2.20462262185),
            (MassUnit.OUNCE, 35.2739619496),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, delta.as_unit(unit))

    def test_add_mass_deltas_produces_mass_delta(self) -> None:
        delta1 = MassDelta(1, MassUnit.KILOGRAM)
        delta2 = MassDelta(2, MassUnit.KILOGRAM)
        new_delta = delta1 + delta2
        self.assertAlmostEqual(3, new_delta.as_unit(MassUnit.KILOGRAM))

    def test_subtract_mass_deltas_produces_mass_delta(self) -> None:
        delta1 = MassDelta(3, MassUnit.KILOGRAM)
        delta2 = MassDelta(2, MassUnit.KILOGRAM)
        new_delta = delta1 - delta2
        self.assertAlmostEqual(1, new_delta.as_unit(MassUnit.KILOGRAM))

    def test_multiply_mass_delta_by_value(self) -> None:
        delta = MassDelta(1, MassUnit.KILOGRAM)
        new_delta_left_mult = 2 * delta
        new_delta_right_mult = delta * 2
        self.assertAlmostEqual(2, new_delta_left_mult.as_unit(MassUnit.KILOGRAM))
        self.assertAlmostEqual(2, new_delta_right_mult.as_unit(MassUnit.KILOGRAM))

    def test_divide_mass_delta_by_value(self) -> None:
        delta = MassDelta(2, MassUnit.KILOGRAM)
        new_delta = delta / 2
        self.assertAlmostEqual(1, new_delta.as_unit(MassUnit.KILOGRAM))

    def test_divide_mass_delta_by_mass_delta_produces_ratio(self) -> None:
        delta1 = MassDelta(2, MassUnit.KILOGRAM)
        delta2 = MassDelta(1, MassUnit.KILOGRAM)
        ratio = delta1 / delta2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_mass_delta(self) -> None:
        delta = MassDelta(1, MassUnit.KILOGRAM)
        new_delta = -delta
        self.assertAlmostEqual(-1, new_delta.as_unit(MassUnit.KILOGRAM))

    def test_absolute_of_mass_delta(self) -> None:
        delta = MassDelta(-1, MassUnit.KILOGRAM)
        new_delta = abs(delta)
        self.assertAlmostEqual(1, new_delta.as_unit(MassUnit.KILOGRAM))

    def test_floor_divide_mass_delta_by_mass_delta_produces_floored_ratio(
        self,
    ) -> None:
        delta1 = MassDelta(3, MassUnit.KILOGRAM)
        delta2 = MassDelta(2, MassUnit.KILOGRAM)
        floored_ratio = delta1 // delta2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_mass_delta_by_mass_delta_produces_ratio_remainder(
        self,
    ) -> None:
        delta1 = MassDelta(3, MassUnit.KILOGRAM)
        delta2 = MassDelta(2, MassUnit.KILOGRAM)
        remainder = delta1 % delta2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_mass_delta_by_mass_delta_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        delta1 = MassDelta(3, MassUnit.KILOGRAM)
        delta2 = MassDelta(2, MassUnit.KILOGRAM)
        floored_ratio, remainder = divmod(delta1, delta2)
        self.assertAlmostEqual(1, floored_ratio)
        self.assertAlmostEqual(1, remainder)

    def test_compare_mass_deltas(self) -> None:
        for (
            mass_delta1,
            mass_delta2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                MassDelta(0, MassUnit.KILOGRAM),
                MassDelta(0, MassUnit.KILOGRAM),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                MassDelta(0, MassUnit.KILOGRAM),
                MassDelta(1, MassUnit.KILOGRAM),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                MassDelta(1, MassUnit.KILOGRAM),
                MassDelta(0, MassUnit.KILOGRAM),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                mass_delta1=mass_delta1,
                mass_delta2=mass_delta2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, mass_delta1 == mass_delta2)
                self.assertEqual(is_not_equal, mass_delta1 != mass_delta2)
                self.assertEqual(is_less_than, mass_delta1 < mass_delta2)
                self.assertEqual(is_less_than_or_equal_to, mass_delta1 <= mass_delta2)
                self.assertEqual(is_greater_than, mass_delta1 > mass_delta2)
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    mass_delta1 >= mass_delta2,
                )
