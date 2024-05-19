#!/usr/bin/env python3
""" module documentation """
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ func doc """
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
        """Func that get page from the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        index = self.index_range(page, page_size)
        return self.dataset()[index[0]:index[1]]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """ return a tuple of size two containing a start and an end index"""
        start_page = (page - 1) * page_size
        end_page = page * page_size
        return (start_page, end_page)
