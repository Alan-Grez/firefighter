"""Geocoding utilities for incident addresses."""

from dataclasses import dataclass


@dataclass(frozen=True)
class GeocodingResult:
    latitude: float | None
    longitude: float | None
    confidence: float | None = None


def geocode_address(address: str, number: str | int | None) -> GeocodingResult:
    """Geocode a street address + number pair.

    Args:
        address: Street name or full address string.
        number: Street number or identifier.

    Returns:
        GeocodingResult placeholder.
    """

    _ = (address, number)
    return GeocodingResult(latitude=None, longitude=None, confidence=None)


def geocode_corner(street_a: str, street_b: str) -> GeocodingResult:
    """Geocode an intersection (corner) between two streets."""

    _ = (street_a, street_b)
    return GeocodingResult(latitude=None, longitude=None, confidence=None)
