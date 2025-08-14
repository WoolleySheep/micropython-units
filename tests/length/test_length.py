import unittest

from units import DistanceUnit, Length, NegativeLengthValueError


class LengthTest(unittest.TestCase):
    """Unit tests for length class."""

    def test_create_length(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Length(1, DistanceUnit.METRE)

    def test_exception_raised_when_creating_length_value_is_negative(
        self,
    ) -> None:
        with self.assertRaises(NegativeLengthValueError) as cm:
            _ = Length(-300, DistanceUnit.METRE)
        self.assertAlmostEqual(-300, cm.exception.value)

    def test_get_length_value_as_unit(self) -> None:
        length = Length(1, DistanceUnit.METRE)

        for unit, expected_value in [
            (DistanceUnit.METRE, 1),
            (DistanceUnit.CENTIMETRE, 100),
            (DistanceUnit.MILLIMETRE, 1_000),
            (DistanceUnit.YARD, 1.09361329834),
            (DistanceUnit.FOOT, 3.28083989501),
            (DistanceUnit.INCH, 39.3700787402),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, length.as_unit(unit))

    def test_compare_lengths(self) -> None:
        for (
            length1,
            length2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                Length(0, DistanceUnit.METRE),
                Length(0, DistanceUnit.METRE),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                Length(0, DistanceUnit.METRE),
                Length(1, DistanceUnit.METRE),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                Length(1, DistanceUnit.METRE),
                Length(0, DistanceUnit.METRE),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                length1=length1,
                length2=length2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, length1 == length2)
                self.assertEqual(is_not_equal, length1 != length2)
                self.assertEqual(is_less_than, length1 < length2)
                self.assertEqual(is_less_than_or_equal_to, length1 <= length2)
                self.assertEqual(is_greater_than, length1 > length2)
                self.assertEqual(is_greater_than_or_equal_to, length1 >= length2)
