#!/usr/bin/env python3
"""Simple pagination"""
import csv
from typing import List


def index_range(page, page_size):
    """Calculate the start and end index for a given page and page size"""
    if not all(isinstance(arg, int) and arg > 0 for arg in (page, page_size)):
        raise ValueError(
                "Both 'page' and 'page_size' should be positive integers.")

    # Calculate start index
    start_index = (page - 1) * page_size

    # Calculate end index
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a specific page of the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int), (
            "Page and page_size should be integers.")
        assert page > 0 and page_size > 0, (
            "Page and page_size should be greater than 0.")

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
