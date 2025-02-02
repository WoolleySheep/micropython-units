import unittest

from units import NegativeTimeValueError, Time, TimeUnit


class TimeTest(unittest.TestCase):
    """Unit tests for time class."""

    def test_create_time(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Time(1, TimeUnit.SECOND)

    def test_exception_raised_when_creating_time_value_is_negative(
        self,
    ) -> None:
        with self.assertRaises(NegativeTimeValueError) as cm:
            _ = Time(-300, TimeUnit.SECOND)
        self.assertAlmostEqual(-300, cm.exception.value)

    def test_get_time_value_as_unit(self) -> None:
        time = Time(1, TimeUnit.SECOND)

        for unit, expected_value in [
            (TimeUnit.SECOND, 1),
            (TimeUnit.MINUTE, 1 / 60),
            (TimeUnit.HOUR, 1 / (60 * 60)),
            (TimeUnit.NANOSECOND, 1e9),
            (TimeUnit.MICROSECOND, 1e6),
            (TimeUnit.MILLISECOND, 1e3),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, time.as_unit(unit))

    def test_compare_times(self) -> None:
        for (
            time1,
            time2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                Time(0, TimeUnit.SECOND),
                Time(0, TimeUnit.SECOND),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                Time(0, TimeUnit.SECOND),
                Time(1, TimeUnit.SECOND),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                Time(1, TimeUnit.SECOND),
                Time(0, TimeUnit.SECOND),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                time1=time1,
                time2=time2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, time1 == time2)
                self.assertEqual(is_not_equal, time1 != time2)
                self.assertEqual(is_less_than, time1 < time2)
                self.assertEqual(is_less_than_or_equal_to, time1 <= time2)
                self.assertEqual(is_greater_than, time1 > time2)
                self.assertEqual(is_greater_than_or_equal_to, time1 >= time2)
