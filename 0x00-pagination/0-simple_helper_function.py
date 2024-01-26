#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page, page_size):
    """Calculate the start and end index for a given page and page size."""
    if not all(isinstance(arg, int) and arg > 0 for arg in (page, page_size)):
        raise ValueError(
                "Both 'page' and 'page_size' should be positive integers.")
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
