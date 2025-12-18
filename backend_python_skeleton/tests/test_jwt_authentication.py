from datetime import timedelta
import time

from app.auth.jwt_authentication import (
    create_access_token,
    verify_access_token
)


def test_jwt_creation_and_verification():
    """
    Demonstrates successful JWT creation and verification
    """

    claims = {
        "sub": "demo@college.edu",
        "email": "demo@college.edu",
        "role": "student"
    }

    token, expiry = create_access_token(claims)

    print("\nGenerated JWT Token:")
    print(token)

    decoded = verify_access_token(token)

    print("\nDecoded JWT Payload:")
    print(decoded)

    assert decoded["email"] == "demo@college.edu"
    assert decoded["role"] == "student"


def test_jwt_expiry_handling():
    """
    Demonstrates token expiration handling
    """

    claims = {
        "sub": "expired@college.edu"
    }

    # Create token that expires in 1 second
    token, _ = create_access_token(
        claims=claims,
    )

    # Force expiry manually (sleep past expiration)
    time.sleep(2)

    try:
        verify_access_token(token)
        assert False, "Expired token should not be valid"
    except ValueError:
        print("\nExpired token correctly rejected.")
