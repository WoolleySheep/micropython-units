import unittest

from units import DistanceUnit, Length, LengthDelta


class LengthAndLengthDeltaTest(unittest.TestCase):
    """Unit tests for interactions between length and length delta classes."""

    def test_add_length_delta_to_length_produces_length(self) -> None:
        length = Length(0, DistanceUnit.METRE)
        delta = LengthDelta(1, DistanceUnit.METRE)
        new_length_left_add = length + delta
        new_length_right_add = delta + length
        self.assertIsInstance(new_length_left_add, Length)
        self.assertAlmostEqual(1, new_length_left_add.as_unit(DistanceUnit.METRE))
        self.assertIsInstance(new_length_right_add, Length)
        self.assertAlmostEqual(1, new_length_right_add.as_unit(DistanceUnit.METRE))

    def test_subtract_length_delta_from_length_produces_length(
        self,
    ) -> None:
        length = Length(1, DistanceUnit.METRE)
        delta = LengthDelta(1, DistanceUnit.METRE)
        new_length = length - delta
        self.assertIsInstance(new_length, Length)
        self.assertAlmostEqual(0, new_length.as_unit(DistanceUnit.METRE))

    def test_subtract_length_from_length_produces_length_delta(
        self,
    ) -> None:
        length1 = Length(3, DistanceUnit.METRE)
        length2 = Length(2, DistanceUnit.METRE)
        new_length_delta = length1 - length2
        self.assertIsInstance(new_length_delta, LengthDelta)
        self.assertAlmostEqual(1, new_length_delta.as_unit(DistanceUnit.METRE))
