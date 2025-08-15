import unittest

from units import Current, CurrentUnit


class CurrentTest(unittest.TestCase):
    """Unit tests for current class."""

    def test_create_current(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Current(1, CurrentUnit.AMPERE)

    def test_get_current_value_as_unit(self) -> None:
        current = Current(1, CurrentUnit.AMPERE)

        for unit, expected_value in [
            (CurrentUnit.AMPERE, 1),
            (CurrentUnit.MILLIAMPERE, 1_000),
            (CurrentUnit.MICROAMPERE, 1_000_000),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, current.as_unit(unit))

    def test_add_currents_produces_current(self) -> None:
        current1 = Current(1, CurrentUnit.AMPERE)
        current2 = Current(2, CurrentUnit.AMPERE)
        new_current = current1 + current2
        self.assertAlmostEqual(3, new_current.as_unit(CurrentUnit.AMPERE))

    def test_subtract_currents_produces_current(self) -> None:
        current1 = Current(3, CurrentUnit.AMPERE)
        current2 = Current(2, CurrentUnit.AMPERE)
        new_current = current1 - current2
        self.assertAlmostEqual(1, new_current.as_unit(CurrentUnit.AMPERE))

    def test_multiply_current_by_value(self) -> None:
        current = Current(1, CurrentUnit.AMPERE)
        new_current_left_mult = 2 * current
        new_current_right_mult = current * 2
        self.assertAlmostEqual(2, new_current_left_mult.as_unit(CurrentUnit.AMPERE))
        self.assertAlmostEqual(2, new_current_right_mult.as_unit(CurrentUnit.AMPERE))

    def test_divide_current_by_value(self) -> None:
        current = Current(2, CurrentUnit.AMPERE)
        new_current = current / 2
        self.assertAlmostEqual(1, new_current.as_unit(CurrentUnit.AMPERE))

    def test_divide_current_by_current_produces_ratio(self) -> None:
        current1 = Current(2, CurrentUnit.AMPERE)
        current2 = Current(1, CurrentUnit.AMPERE)
        ratio = current1 / current2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_current(self) -> None:
        current = Current(1, CurrentUnit.AMPERE)
        new_current = -current
        self.assertAlmostEqual(-1, new_current.as_unit(CurrentUnit.AMPERE))

    def test_absolute_of_current(self) -> None:
        current = Current(-1, CurrentUnit.AMPERE)
        new_current = abs(current)
        self.assertAlmostEqual(1, new_current.as_unit(CurrentUnit.AMPERE))

    def test_floor_divide_current_by_current_produces_floored_ratio(
        self,
    ) -> None:
        current1 = Current(3, CurrentUnit.AMPERE)
        current2 = Current(2, CurrentUnit.AMPERE)
        floored_ratio = current1 // current2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_current_by_current_produces_ratio_remainder(
        self,
    ) -> None:
        current1 = Current(3, CurrentUnit.AMPERE)
        current2 = Current(2, CurrentUnit.AMPERE)
        remainder = current1 % current2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_current_by_current_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        current1 = Current(3, CurrentUnit.AMPERE)
        current2 = Current(2, CurrentUnit.AMPERE)
        floored_ratio, remainder = divmod(current1, current2)
        self.assertAlmostEqual(1, floored_ratio)
        self.assertAlmostEqual(1, remainder)

    def test_compare_currents(self) -> None:
        for (
            current1,
            current2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                Current(0, CurrentUnit.AMPERE),
                Current(0, CurrentUnit.AMPERE),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                Current(0, CurrentUnit.AMPERE),
                Current(1, CurrentUnit.AMPERE),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                Current(1, CurrentUnit.AMPERE),
                Current(0, CurrentUnit.AMPERE),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                current1=current1,
                current2=current2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, current1 == current2)
                self.assertEqual(is_not_equal, current1 != current2)
                self.assertEqual(is_less_than, current1 < current2)
                self.assertEqual(is_less_than_or_equal_to, current1 <= current2)
                self.assertEqual(is_greater_than, current1 > current2)
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    current1 >= current2,
                )
