import re


def validate_password_strength(password: str) -> str:
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")

    patterns = [
        (r"[A-Z]", "Password must contain at least one uppercase letter"),
        (r"[a-z]", "Password must contain at least one lowercase letter"),
        (r"\d", "Password must contain at least one digit"),
        (r"[!@#$%^&*(),.?\":{}|<>]", "Password must contain at least one special character"),
    ]
    for pattern, msg in patterns:
        if not re.search(pattern, password):
            raise ValueError(msg)

    return password
