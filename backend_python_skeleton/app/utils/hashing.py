"""
hashing.py

Utility functions for password hashing and verification.
Pure utility module with no framework or database dependencies.
"""

import hashlib
import os
from typing import Tuple


def hash_password(password: str) -> Tuple[str, str]:
    """
    Hash a password using SHA-256 with a random salt.

    Args:
        password (str): Plain text password

    Returns:
        Tuple[str, str]: (hashed_password, salt)
    """

    if not password:
        raise ValueError("Password cannot be empty")

    salt = os.urandom(16).hex()
    salted_password = (password + salt).encode("utf-8")

    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password, salt


def verify_password(
    password: str,
    stored_hash: str,
    salt: str
) -> bool:
    """
    Verify a password against the stored hash and salt.

    Args:
        password (str): Input password
        stored_hash (str): Stored hashed password
        salt (str): Stored salt

    Returns:
        bool: True if password matches, False otherwise
    """

    if not password or not stored_hash or not salt:
        return False

    salted_password = (password + salt).encode("utf-8")
    computed_hash = hashlib.sha256(salted_password).hexdigest()

    return computed_hash == stored_hash
