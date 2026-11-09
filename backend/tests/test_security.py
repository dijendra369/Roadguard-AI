from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    verify_access_token
)


def test_password_hashing():
    password = "RoadGuard@2026"

    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed)


def test_wrong_password():
    password = "RoadGuard@2026"
    hashed = hash_password(password)

    assert not verify_password("WrongPassword", hashed)


def test_jwt_token_creation():
    token = create_access_token({
        "sub": "3",
        "role": "user"
    })

    payload = verify_access_token(token)

    assert payload is not None
    assert payload["sub"] == "3"
    assert payload["role"] == "user"