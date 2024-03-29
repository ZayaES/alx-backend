#!/usr/bin/env python3
"""module containing index_range"""


def index_range(page: int, page_size: int) -> tuple:
    return ((page - 1) * page_size, page * page_size)
