import unittest

from src.calculate_kpi import (
    DEFAULT_DISTANCE_KM,
    DEFAULT_FUEL_LITERS,
    calculate_mileage,
)


class TestMathUtils(unittest.TestCase):
    def test_calculate_mileage(self) -> None:
        self.assertEqual(
            calculate_mileage(DEFAULT_DISTANCE_KM, DEFAULT_FUEL_LITERS),
            DEFAULT_DISTANCE_KM / DEFAULT_FUEL_LITERS,
        )

    def test_calculate_mileage_zero_fuel(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            calculate_mileage(120, 0)


if __name__ == "__main__":
    unittest.main()
