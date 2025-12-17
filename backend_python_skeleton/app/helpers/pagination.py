"""
pagination.py

Helper utilities for paginating lists of data.
Pure logic, no framework or database dependencies.
"""

from typing import List, Any, Dict


def paginate(
    items: List[Any],
    page: int = 1,
    page_size: int = 10
) -> Dict[str, Any]:
    """
    Paginate a list of items using page number and page size.

    Args:
        items (List[Any]): Full list of items
        page (int): Page number (1-indexed)
        page_size (int): Number of items per page

    Returns:
        Dict[str, Any]: Paginated response with metadata
    """

    if page < 1:
        page = 1
    if page_size < 1:
        page_size = 10

    total_items = len(items)
    total_pages = (total_items + page_size - 1) // page_size

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    paginated_items = items[start_index:end_index]

    return {
        "page": page,
        "page_size": page_size,
        "total_items": total_items,
        "total_pages": total_pages,
        "items": paginated_items
    }


def paginate_offset_limit(
    items: List[Any],
    offset: int = 0,
    limit: int = 10
) -> Dict[str, Any]:
    """
    Paginate a list using offset-limit style pagination.

    Args:
        items (List[Any]): Full list of items
        offset (int): Starting index
        limit (int): Number of items to return

    Returns:
        Dict[str, Any]: Paginated response with metadata
    """

    if offset < 0:
        offset = 0
    if limit < 1:
        limit = 10

    total_items = len(items)
    sliced_items = items[offset: offset + limit]

    return {
        "offset": offset,
        "limit": limit,
        "total_items": total_items,
        "items": sliced_items
    }
