"""
formatters.py

Helper utilities to format API responses and data objects.
Pure functions with no external dependencies.
"""

from typing import Any, Dict, List


def success_response(
    data: Any,
    message: str = "Success"
) -> Dict[str, Any]:
    """
    Standard success response format.
    """
    return {
        "status": "success",
        "message": message,
        "data": data
    }


def error_response(
    message: str,
    error_code: int = 400
) -> Dict[str, Any]:
    """
    Standard error response format.
    """
    return {
        "status": "error",
        "message": message,
        "error_code": error_code
    }


def format_list(
    items: List[Dict[str, Any]],
    allowed_fields: List[str]
) -> List[Dict[str, Any]]:
    """
    Filter and format a list of dictionaries
    by keeping only allowed fields.

    Args:
        items (List[Dict]): Input list
        allowed_fields (List[str]): Keys to retain

    Returns:
        List[Dict]: Formatted list
    """

    formatted = []

    for item in items:
        formatted.append(
            {key: item.get(key) for key in allowed_fields}
        )

    return formatted


def format_single(
    item: Dict[str, Any],
    allowed_fields: List[str]
) -> Dict[str, Any]:
    """
    Format a single dictionary by keeping allowed fields.
    """

    return {key: item.get(key) for key in allowed_fields}
