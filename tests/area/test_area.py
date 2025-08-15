import unittest

from src.units import Area, AreaUnit, NegativeAreaValueError


class AreaTest(unittest.TestCase):
    """Unit tests for area class."""

    def test_create_area(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Area(1, AreaUnit.SQUARE_METRE)

    def test_exception_raised_when_creating_area_value_is_negative(
        self,
    ) -> None:
        with self.assertRaises(NegativeAreaValueError) as cm:
            _ = Area(-300, AreaUnit.SQUARE_METRE)
        self.assertAlmostEqual(-300, cm.exception.value)

    def test_get_area_value_as_unit(self) -> None:
        area = Area(1, AreaUnit.SQUARE_METRE)

        for unit, expected_value in [
            (AreaUnit.SQUARE_METRE, 1),
            (AreaUnit.SQUARE_CENTIMETRE, 1e4),
            (AreaUnit.SQUARE_MILLIMETRE, 1e6),
            (AreaUnit.SQUARE_YARD, 1.09361329834**2),
            (AreaUnit.SQUARE_FOOT, 3.28083989501**2),
            (AreaUnit.SQUARE_INCH, 39.3700787402**2),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, area.as_unit(unit))

    def test_compare_areas(self) -> None:
        for (
            area1,
            area2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                Area(0, AreaUnit.SQUARE_METRE),
                Area(0, AreaUnit.SQUARE_METRE),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                Area(0, AreaUnit.SQUARE_METRE),
                Area(1, AreaUnit.SQUARE_METRE),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                Area(1, AreaUnit.SQUARE_METRE),
                Area(0, AreaUnit.SQUARE_METRE),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                area1=area1,
                area2=area2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, area1 == area2)
                self.assertEqual(is_not_equal, area1 != area2)
                self.assertEqual(is_less_than, area1 < area2)
                self.assertEqual(is_less_than_or_equal_to, area1 <= area2)
                self.assertEqual(is_greater_than, area1 > area2)
                self.assertEqual(is_greater_than_or_equal_to, area1 >= area2)
