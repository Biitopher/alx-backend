#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""
import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieve hyperlinked information based specified start
        index and page size."""
        assert isinstance(index, int) or index is None, (
                "Index should be an integer or None.")
        assert isinstance(page_size, int), "Page_size should be an integer."
        assert page_size > 0, "Page_size should be greater than 0."

        dataset = self.dataset()

        if index is None:
            index = 0

        assert 0 <= index < len(dataset), "Index is out of range."

        end_index = min(index + page_size, len(dataset))

        data = dataset[index:end_index]

        next_index = end_index

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
