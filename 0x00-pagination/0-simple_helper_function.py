#!/usr/bin/env python3
"""
Module documentation
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function documentation
    """
    start, end = 0, 0
    for j in range(page):
        start = end
        end += page_size

    return (start, end)
