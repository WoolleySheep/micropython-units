import unittest

from src.units import Time, TimeDelta, TimeUnit


class TimeAndTimeDeltaTest(unittest.TestCase):
    """Unit tests for interactions between time and time delta classes."""

    def test_add_time_delta_to_time_produces_time(self) -> None:
        time = Time(0, TimeUnit.SECOND)
        delta = TimeDelta(1, TimeUnit.SECOND)
        new_time_left_add = time + delta
        new_time_right_add = delta + time
        self.assertIsInstance(new_time_left_add, Time)
        self.assertAlmostEqual(1, new_time_left_add.as_unit(TimeUnit.SECOND))
        self.assertIsInstance(new_time_right_add, Time)
        self.assertAlmostEqual(1, new_time_right_add.as_unit(TimeUnit.SECOND))

    def test_subtract_time_delta_from_time_produces_time(
        self,
    ) -> None:
        time = Time(1, TimeUnit.SECOND)
        delta = TimeDelta(1, TimeUnit.SECOND)
        new_time = time - delta
        self.assertIsInstance(new_time, Time)
        self.assertAlmostEqual(0, new_time.as_unit(TimeUnit.SECOND))

    def test_subtract_time_from_time_produces_time_delta(
        self,
    ) -> None:
        time1 = Time(3, TimeUnit.SECOND)
        time2 = Time(2, TimeUnit.SECOND)
        new_time_delta = time1 - time2
        self.assertIsInstance(new_time_delta, TimeDelta)
        self.assertAlmostEqual(1, new_time_delta.as_unit(TimeUnit.SECOND))
