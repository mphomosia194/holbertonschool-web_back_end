#!/usr/bin/env python3
"""Module containing a multiplier factory function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiply(value: float) -> float:
        return value * multiplier

    return multiply
