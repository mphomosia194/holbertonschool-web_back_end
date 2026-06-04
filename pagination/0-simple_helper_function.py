#!/usr/bin/env python3
"""Module containing pagination helper function."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return start and end indexes for a pagination page."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
