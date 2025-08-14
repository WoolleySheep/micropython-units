import unittest

from units import Mass, MassDelta, MassUnit


class MassAndMassDeltaTest(unittest.TestCase):
    """Unit tests for interactions between mass and mass delta classes."""

    def test_add_mass_delta_to_mass_produces_mass(self) -> None:
        mass = Mass(0, MassUnit.KILOGRAM)
        delta = MassDelta(1, MassUnit.KILOGRAM)
        new_mass_left_add = mass + delta
        new_mass_right_add = delta + mass
        self.assertIsInstance(new_mass_left_add, Mass)
        self.assertAlmostEqual(1, new_mass_left_add.as_unit(MassUnit.KILOGRAM))
        self.assertIsInstance(new_mass_right_add, Mass)
        self.assertAlmostEqual(1, new_mass_right_add.as_unit(MassUnit.KILOGRAM))

    def test_subtract_mass_delta_from_mass_produces_mass(
        self,
    ) -> None:
        mass = Mass(1, MassUnit.KILOGRAM)
        delta = MassDelta(1, MassUnit.KILOGRAM)
        new_mass = mass - delta
        self.assertIsInstance(new_mass, Mass)
        self.assertAlmostEqual(0, new_mass.as_unit(MassUnit.KILOGRAM))

    def test_subtract_mass_from_mass_produces_mass_delta(
        self,
    ) -> None:
        mass1 = Mass(3, MassUnit.KILOGRAM)
        mass2 = Mass(2, MassUnit.KILOGRAM)
        new_mass_delta = mass1 - mass2
        self.assertIsInstance(new_mass_delta, MassDelta)
        self.assertAlmostEqual(1, new_mass_delta.as_unit(MassUnit.KILOGRAM))
