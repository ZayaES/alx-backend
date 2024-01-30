#!/usr/bin/env python3
"""implements a hypermedia pagination"""
import csv
import math
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """returns the start and end index of the page
    Args:
        page: page number
        page_size: page size, number of rows in a page
    Returns:
        start and end index (tuple)"""

    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """initializes an instance"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """gets the data in a page"""

        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        all_data = self.dataset()
        ind_range = index_range(page, page_size)
        required_data = all_data[ind_range[0]:ind_range[1]]

        return required_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """gets data and includes some info"""

        page_data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size + 1
        page_dict = {
            'page_size': page_size if page_size
            <= len(page_data) else len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page + 1 <= total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
             }
        return page_dict
