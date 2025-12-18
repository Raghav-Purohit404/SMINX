from app.auth.jwt_authentication import (
    create_access_token,
    verify_access_token
)


def demo_jwt_authentication():
    """
    Demonstrates JWT creation and verification with visible output
    """

    print("\n========== JWT AUTHENTICATION DEMO ==========")

    # Sample claims
    claims = {
        "sub": "demo@college.edu",
        "email": "demo@college.edu",
        "role": "student"
    }

    # Create JWT
    token, expiry = create_access_token(claims)

    print("\nGenerated JWT Token:")
    print(token)

    print("\nToken Expiry Time:")
    print(expiry)

    # Verify JWT
    decoded = verify_access_token(token)

    print("\nDecoded JWT Payload:")
    for key, value in decoded.items():
        print(f"{key}: {value}")

    print("\nJWT verification successful ")
    print("============================================\n")


# Allows direct execution with `python`
if __name__ == "__main__":
    demo_jwt_authentication()

