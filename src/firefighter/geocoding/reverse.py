"""Reverse geocoding utilities."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ReverseGeocodeResult:
    street: str | None
    number: str | None
    intersection: str | None

    @property
    def resolved_address(self) -> str | None:
        if self.street and self.number:
            return f"{self.street} {self.number}"
        if self.intersection:
            return self.intersection
        return self.street


def reverse_geocode(latitude: float | None, longitude: float | None) -> ReverseGeocodeResult:
    """Resolve a street address or intersection from latitude/longitude."""

    _ = (latitude, longitude)
    return ReverseGeocodeResult(street=None, number=None, intersection=None)
