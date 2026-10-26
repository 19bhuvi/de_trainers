"""Sample math utility functions."""

DEFAULT_DISTANCE_KM = 450
DEFAULT_FUEL_LITERS = 0


def calculate_mileage(distance_km: float, fuel_liters: float) -> float:
    """Return mileage in km/L.

    Raises ZeroDivisionError if fuel_liters is zero.
    """
    if fuel_liters == 0:
        raise ZeroDivisionError("fuel_liters cannot be zero for mileage calculation")
    return distance_km / fuel_liters


if __name__ == "__main__":
    result = calculate_mileage(DEFAULT_DISTANCE_KM, DEFAULT_FUEL_LITERS)
    print(f"Mileage: {result} km/L")