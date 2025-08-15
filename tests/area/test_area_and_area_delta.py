import unittest

from units import Area, AreaDelta, AreaUnit


class AreaAndAreaDeltaTest(unittest.TestCase):
    """Unit tests for interactions between area and area delta classes."""

    def test_add_area_delta_to_area_produces_area(self) -> None:
        area = Area(0, AreaUnit.SQUARE_METRE)
        delta = AreaDelta(1, AreaUnit.SQUARE_METRE)
        new_area_left_add = area + delta
        new_area_right_add = delta + area
        self.assertIsInstance(new_area_left_add, Area)
        self.assertAlmostEqual(1, new_area_left_add.as_unit(AreaUnit.SQUARE_METRE))
        self.assertIsInstance(new_area_right_add, Area)
        self.assertAlmostEqual(1, new_area_right_add.as_unit(AreaUnit.SQUARE_METRE))

    def test_subtract_area_delta_from_area_produces_area(
        self,
    ) -> None:
        area = Area(1, AreaUnit.SQUARE_METRE)
        delta = AreaDelta(1, AreaUnit.SQUARE_METRE)
        new_area = area - delta
        self.assertIsInstance(new_area, Area)
        self.assertAlmostEqual(0, new_area.as_unit(AreaUnit.SQUARE_METRE))

    def test_subtract_area_from_area_produces_area_delta(
        self,
    ) -> None:
        area1 = Area(3, AreaUnit.SQUARE_METRE)
        area2 = Area(2, AreaUnit.SQUARE_METRE)
        new_area_delta = area1 - area2
        self.assertIsInstance(new_area_delta, AreaDelta)
        self.assertAlmostEqual(1, new_area_delta.as_unit(AreaUnit.SQUARE_METRE))
